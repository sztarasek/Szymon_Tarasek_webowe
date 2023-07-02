from enum import Enum

from pydantic import BaseModel

class OrderCreateSchema(BaseModel):
    customer_id: int
    products_id: int
    quantity: int

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "products_id": 1,
                "quantity": 1,
            }
        }


class OrderUpdateSchema(BaseModel):
    customer_id: int
    products_id: int
    quantity: int

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "products_id": 1,
                "quantity": 2
            }
        }


class Order(OrderCreateSchema):
    id: int

