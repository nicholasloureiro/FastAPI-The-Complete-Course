from sys import prefix
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.database import create_db
from app.routers import auth, requester, kitchen

app = FastAPI()

create_db()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router)
app.include_router(requester.router, prefix='/requester')
app.include_router(kitchen.router, prefix='/kitchen')



             
