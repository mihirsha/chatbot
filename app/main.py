from fastapi import FastAPI
from app.controller import UserController
import app.auth as auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(UserController.router)


@app.get('/')
async def root():
    return {"message": "Hey this is Backend testing"}
