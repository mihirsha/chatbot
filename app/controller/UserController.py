from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from app.schemas import Signup
from app.service.UserService import *
from app.schemas import *

router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def signup(user: Signup, db:  Session = Depends(get_db)):
    return UserService.signup(user, db)
