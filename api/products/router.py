from fastapi import APIRouter, HTTPException, Query

from .storage import get_products_storage
from .schema import ProductCreateSchema, ProductUpdateSchema, Product

router = APIRouter()


PRODUCTS_STORAGE = get_products_storage()


@router.get("/")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())


@router.get("/{product_id}")
async def get_product(product_id: int) -> Product:
    try:
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

#Do pomyślenia
@router.patch("/{product_id}")
async def update_product(
    product_id: int, updated_product: ProductUpdateSchema
) -> Product:
    try:
        new = Product(**(PRODUCTS_STORAGE[product_id].dict() | updated_product.dict(exclude_unset=True)))
        PRODUCTS_STORAGE[product_id] = new
        return PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code = 404, detail=f"Product with ID={product_id} does not exist."
        )



@router.delete("/{product_id}")
async def delete_product(product_id: int) -> None:
    try:
        del PRODUCTS_STORAGE[product_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Product with ID={product_id} does not exist."
        )

#Do pomyślenia
@router.post("/")
async def create_product(product: ProductCreateSchema) -> Product:
    product_id = len(PRODUCTS_STORAGE)

    PRODUCTS_STORAGE[product_id] = Product(id=product_id, **product.dict())

    return PRODUCTS_STORAGE[product_id]
