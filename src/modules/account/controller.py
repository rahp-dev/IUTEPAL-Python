from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .service import AccountService
from fastapi.responses import HTMLResponse, RedirectResponse

templates = Jinja2Templates(directory="src/modules/views/templates")
account_router = APIRouter()

account_service = AccountService()

@account_router.get("/account", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    transactions, total_amount = account_service.get_transactions()
    return templates.TemplateResponse("index.html", {"request": request, "transactions": transactions, "total_amount": total_amount})

@account_router.post("/create-account", response_class=HTMLResponse)
async def post_dashboard(request: Request, transactionType:str=Form(...), amount: float = Form(...),description:str=Form(...)):
    
    await account_service.create_transaction(transactionType,amount, description)
    return RedirectResponse(url="/dashboard", status_code=303)
