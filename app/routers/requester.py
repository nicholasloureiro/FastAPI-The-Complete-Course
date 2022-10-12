import sys
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, APIRouter, Request
from app import models
from app.database import engine, SessionLocal
from sqlalchemy.orm import Session
from .auth import get_current_user
from datetime import date
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    tags=["Requester"],
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

    requester = db.query(models.Requester).filter(models.Requester.owner_id == user.get("id")).all()

    return templates.TemplateResponse("confirmaçao.html", {"request": request, "requester": requester, "user": user})


@router.get("/confirmaçao", response_class=HTMLResponse)
async def add_new_todo(request: Request, user=Depends(get_current_user)):
    
    days = date.today().weekday()
    week = ['Segunda','Terça','Quarta','Quinta', 'Sexta']
    while days < 5:
        days += 1
                                
                                
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("confirmaçao.html", {"request": request, "user": user, "week": week,"days":days})


@router.get("/attendance/{id}", response_class=HTMLResponse)
async def complete_todo(request: Request, id: int, db: Session = Depends(get_db)):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    requester = db.query(models.Requester).filter(models.Requester.id == id).first()

    requester.attendance = not requester.attendance

    db.add(requester)
    db.commit()

    return RedirectResponse(url="/confirmaçao", status_code=status.HTTP_302_FOUND)


