from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from fastapi import FastAPI, Request, Form, Depends, HTTPException,APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional

from src.modules.account.service import AccountService
from src.modules.user.service.UserService import UserService
from src.modules.user.scheme.UserScheme import CreateUser,User

from src.modules.auth.service.AuthService import get_user_current, get_user_disabled_current

viewRouter = APIRouter()
# Configurar Jinja2 para manejar las plantillas HTML
templates = Jinja2Templates(directory="src\\modules\\views\\templates")
userService = UserService()
accountService = AccountService()
# Ruta para la vista web
@viewRouter.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {"request": request, "message": "Hola desde FastAPI!"}
    print(request)
    return templates.TemplateResponse("index.html", context)



@viewRouter.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@viewRouter.post("/register")
async def register_user(request: Request, username: str = Form(...), confirm_password: str = Form(...), password: str = Form(...), full_name: str = Form(...), email: str = Form(...)):
    
    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Las contraseñas no coinciden")
    
    user_data = CreateUser(
        username=username,
        password=password,
        full_name=full_name,
        email=email,
        
        disabled=False
    )
    
    # Debugging
    print("User data:", user_data)
    
    user = await userService.create_user(user_data)
    
    # Debugging
    print("Created user:", user)
    
    return RedirectResponse(url="/", status_code=302)


# Ruta de dashboard (nueva plantilla)
@viewRouter.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    
    token: Optional[str] = request.cookies.get("access_token")
    transactions = await accountService.get_all_transactions()
    total_amount = sum(t.amount if t.transactionType == 'Depósito' else - t.amount for t in transactions)
    total_ingresos = sum(t.amount for t in transactions if t.transactionType == 'Depósito')
    total_egresos = sum(t.amount for t in transactions if t.transactionType == 'Retiro')


    if not token:
        return RedirectResponse(url="/", status_code=302)
    context = {"request": request, "token": token, "transactions": transactions,'total_amount': total_amount, 'total_ingresos':total_ingresos,'total_egresos':total_egresos}
    return templates.TemplateResponse("dashboard.html", context)
