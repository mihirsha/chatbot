from app.schema.UserSchema import Signup
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from app.models import User
from app.utils import hash


class UserService:

    def signup(user: Signup,  db:  Session):
        if (user.email == None or user.email.strip() == "" or user.name == None or user.name.strip() == "" or
                user.password == None or user.password.strip() == ""):

            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Incomplete information")

        user_fetched = db.query(User).filter(user.email == User.email).first()

        if user_fetched is not None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Account {user.email} already present")
        else:
            hashed_password = hash(user.password)
            user.password = hashed_password
            new_user = User(**user.dict())

            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user

    def getUser(email: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if user == None:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Account {email} does not exists")
        return user
