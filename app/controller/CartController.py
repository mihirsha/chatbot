from fastapi import status, Depends, APIRouter
from app.database.database import get_db
from app.service.CartService import *
from app.schema.CartSchema import *

router = APIRouter(
    prefix="/cart",
    tags=['Cart']
)


@router.post("/addItems", status_code=status.HTTP_201_CREATED)
async def add_items_to_the_cart(request: CartInputs, db:  Session = Depends(get_db)):
    return CartService.addItemCart(request, db)
