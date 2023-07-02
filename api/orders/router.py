from fastapi import APIRouter, HTTPException, Query

from .storage import get_orders_storage
from .schema import OrderCreateSchema, OrderUpdateSchema, Order

router = APIRouter()


ORDERS_STORAGE = get_orders_storage()


@router.get("/")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())


@router.get("/{order_id}")
async def get_order(order_id: int) -> Order:
    try:
        return ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

#Do pomyślenia
@router.patch("/{order_id}")
async def update_order(
    order_id: int, updated_order: OrderUpdateSchema
) -> Order:
    try:
        new = Order(**(ORDERS_STORAGE[order_id].dict() | updated_order.dict(exclude_unset=True)))
        ORDERS_STORAGE[order_id] = new
        return ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code = 404, detail=f"Order with ID={order_id} does not exist."
        )



@router.delete("/{order_id}")
async def delete_order(order_id: int) -> None:
    try:
        del ORDERS_STORAGE[order_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID={order_id} does not exist."
        )

#Do pomyślenia
@router.post("/")
async def create_order(order: OrderCreateSchema) -> Order:
    order_id = len(ORDERS_STORAGE)

    ORDERS_STORAGE[order_id] = Order(id=order_id, **order.dict())

    return ORDERS_STORAGE[order_id]
