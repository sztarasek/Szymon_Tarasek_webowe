from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage
from .schema import CustomerCreateSchema, CustomerUpdateSchema, Customer

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()


@router.get("/")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())


@router.get("/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

#Do pomyślenia
@router.patch("/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
    try:
        new = Customer(**(CUSTOMERS_STORAGE[customer_id].dict() | updated_customer.dict(exclude_unset=True)))
        CUSTOMERS_STORAGE[customer_id] = new
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code = 404, detail=f"Customer with ID={customer_id} does not exist."
        )



@router.delete("/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

#Do pomyślenia
@router.post("/")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
    customer_id = len(CUSTOMERS_STORAGE)

    CUSTOMERS_STORAGE[customer_id] = Customer(id=customer_id, **customer.dict())

    return CUSTOMERS_STORAGE[customer_id]
