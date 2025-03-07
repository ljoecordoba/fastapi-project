from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

product_list = [Product(id=1, name="Product 1", description="Description 1", price=100.0),
                Product(id=2, name="Product 2", description="Description 2", price=200.0),
                Product(id=3, name="Product 3", description="Description 3", price=300.0)]

router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"description": "Not found"}})


@router.get("/")
async def products():
    return product_list

@router.get("/{product_id}")
async def product(id: int):
    return product_list[id]