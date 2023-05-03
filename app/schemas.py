from typing import Optional
from pydantic import BaseModel


class Signup(BaseModel):
    email: str
    password: str
    phoneNumber: str
    name: str


class Userlogin(BaseModel):
    email: str
    password: str


class TokenData(BaseModel):
    id: Optional[str] = None


class UserOut(BaseModel):
    token: str = None
    name: str
    email: str
    phoneNumber: str

    class Config:
        orm_mode = True


class Book(BaseModel):
    title: str
    description: Optional[str] = None
    authors: list[int]


class Author(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BookOut(BaseModel):
    title: str
    description: Optional[str] = None
    authors: list[Author]

    class Config:
        orm_mode = True
