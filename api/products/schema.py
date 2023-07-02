from enum import Enum

from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
    name: str
    price: int

    class Config:
        schema_extra = {
            "example": {
                "name": "Toster",
                "price": 299,
            }
        }


class ProductUpdateSchema(BaseModel):
    name: str | None
    price: int | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Toster",
                "price": 199
            }
        }


class Product(ProductCreateSchema):
    id: int

