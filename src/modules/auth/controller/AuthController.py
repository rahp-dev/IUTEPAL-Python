from fastapi import APIRouter ,requests ,Request
from fastapi import FastAPI,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.modules.auth.service.AuthService import authenticate_user,get_users_db,create_token
from datetime import timedelta
from fastapi.responses import HTMLResponse, RedirectResponse
authRouter = APIRouter()

@authRouter.post("/auth-login")
async def login(form_data:OAuth2PasswordRequestForm = Depends()):
    
    users_db = await get_users_db()
    user = authenticate_user(users_db, form_data.username, form_data.password)
    
    access_token_expire = timedelta(minutes=30)
    
    access_token_jwt = create_token({"sub":user.username},access_token_expire)
    
    return {
        "access_token": access_token_jwt,
        "token_type": "bearer"
    }

# Ruta de autenticación
@authRouter.post("/auth-login-view")
async def loginView(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    
    
    accessTokenData = await login(form_data) 
    
    response = RedirectResponse(url="/dashboard", status_code=302)
    response.headers["Authorization"] = f"Bearer {accessTokenData['access_token']}"
    response.headers["token_type"] = "bearer"
    response.set_cookie("access_token",f'{accessTokenData['access_token']}')
    return response
