import sys
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse
from datetime import date
from fastapi import Depends, APIRouter, Request, Form
from app import models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from .auth import get_current_user

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    tags=["Kitchen"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
async def read_all_by_user(request: Request, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    kitchen = db.query(models.Users).filter(models.Users.id == user.get("id")).all()

    return templates.TemplateResponse("confirmaçao.html", {"request": request, "kitchen": kitchen, "user": user})


@router.get("/cardapio", response_class=HTMLResponse)
async def menu(request: Request):
    return templates.TemplateResponse("kitchen.html", {"request":request})


@router.post("/cardapio", response_class=HTMLResponse)
async def add_menu(
    request: Request,
    menu: str = Form(...),
    db: Session = Depends(get_db),
):

    kit_model = models.Kitchen()
    kit_model.menu = menu 
    db.add(kit_model)
    db.commit()

    return RedirectResponse(url="/confirmaçao", status_code=status.HTTP_302_FOUND)
