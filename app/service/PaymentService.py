from sqlalchemy.orm import Session
from sqlalchemy import delete
from fastapi import status, HTTPException
from app.models import Books, BookDetails, CartItems, User
from app.schema.PaymentSchema import PaymentInput
from datetime import datetime, timedelta


class PaymentService:

    def paymentAdd(email: str, db: Session):
        """
            -> check bookDetail availability is True
            -> bookDetail availability turn false
            -> updating user id in book table
            -> clear cart

        """
        # expire = datetime.utcnow() + timedelta(days=)

        user = db.query(User).filter(User.email == email).first()
        bookFetch = db.query(CartItems).filter(
            CartItems.user_id == user.id).all()

        if bookFetch == []:
            raise HTTPException(
                status_code=status.HTTP_200_OK, detail=f"No Books in cart to be checkedout")

        for book in bookFetch:
            bookDetail = db.query(BookDetails).filter(
                BookDetails.book_id == book.book_id).first()
            if bookDetail is None:
                raise HTTPException(
                    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Book detail for book id {book.book_id} not available")

            if bookDetail.availability == False:
                raise HTTPException(
                    status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Book with id {book.book_id} is already taken kindly delete it from your cart")

        for book in bookFetch:

            singleBook = db.query(Books).filter(
                Books.id == book.book_id).first()
            singleBook.bookDetail.availability = False
            singleBook.bookDetail.rented_day = datetime.utcnow()
            singleBook.bookDetail.release_day = datetime.utcnow() + \
                timedelta(days=book.rental_period)
            singleBook.user_id = user.id

            details = db.query(BookDetails).filter(
                BookDetails.book_id == book.book_id).first()
            details.rented_day = datetime.utcnow()
            details.release_day = datetime.utcnow() + timedelta(days=book.rental_period)
            db.add(singleBook)
            db.commit()

            db.add(details)
            db.commit()

        items = db.query(CartItems).filter(CartItems.user_id == user.id).all()
        for item in items:
            db.delete(item)
            db.commit()
        return "payment done"

    def releaseBooks(email: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        books: list[Books] = db.query(Books).filter(
            Books.user_id == user.id).all()

        for i in range(len(books)):

            books[i].userRented = None
            books[i].bookDetail[0].availability = True

            books[i].bookDetail[0].rented_day = None
            books[i].bookDetail[0].release_day = None

            db.add(books[i])
            db.commit()

        return