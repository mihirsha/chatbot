from typing import Optional
from pydantic import BaseModel


class Signup(BaseModel):
    email: str
    password: str
    name: str


class Userlogin(BaseModel):
    email: str
    password: str


class TokenData(BaseModel):
    id: Optional[str] = None

class UserOut(BaseModel):
    id: int
    token: Optional[str] = None
    name: str
    email: str

    class Config:
        from_attributes = True


class UserOutLogin(BaseModel):
    token: Optional[str] = None
    name: str
    email: str

    class Config:
        from_attributes = True
