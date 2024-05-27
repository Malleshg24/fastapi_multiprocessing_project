from fastapi import FastAPI
from app.views.add_view import router as add_router

app = FastAPI()

app.include_router(add_router, prefix="/add", tags=["add"])
