from typing import Optional
from pydantic import BaseModel


class updateBookUser(BaseModel):
    user_id: int
    book_id: int


class Genres(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


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


class Book(BaseModel):
    title: str
    description: Optional[str] = None
    authors: list[int]
    genres: list[int]


class BookOutForAuthor(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genres: list[Genres]

    class Config:
        orm_mode = True


class AuthorForGet(BaseModel):
    id: int
    name: str
    books: list[BookOutForAuthor]

    class Config:
        orm_mode = True


class Author(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserOutBokResponse(BaseModel):
    name: str
    email: str
    phoneNumber: str

    class Config:
        orm_mode = True


class BookOutForGenre(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    authors: list[Author]

    class Config:
        orm_mode = True


class GenresResponse(BaseModel):
    id: int
    name: str
    books: list[BookOutForGenre]

    class Config:
        orm_mode: True


class BookOut(BaseModel):
    title: str
    description: Optional[str] = None
    authors: list[Author]
    genres: list[Genres]

    class Config:
        orm_mode = True


class BookResponse(BaseModel):
    title: str
    description: Optional[str] = None
    authors: list[Author]
    genres: list[Genres]
    userRented: Optional[UserOutBokResponse] = None

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    token: Optional[str] = None
    name: str
    email: str
    phoneNumber: str
    books: list[BookOut]

    class Config:
        orm_mode = True
