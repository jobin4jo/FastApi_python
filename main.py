from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4
app= FastAPI(
    title="NEXUS_API",
    description="API for NEXUS",
    version="1.0.0"
)
item = []
@app.get("/products")
def products():
    return [
        {
            "id": 1,
            "name": "Product 1",
            "price": 10.0
        },
        {
            "id": 2,
            "name": "Product 2",
            "price": 20.0
        }
    ]
# @app.get("/products/{product_id}")
# def product(product_id: int):
#     return {
#         "id": product_id,
#         "name": f"Product {product_id}",
#         "price": 10.0 * product_id
#     }

user_router = APIRouter(prefix='/user')

@user_router.get('')
def get_user():
    return {"message": "User data"}

class Product(BaseModel):
    id:int
    name: str
    price: float
    description: str = None
@app.post("/products/new")
def create_product(product: Product):
   itemreques= {"id":product.id,"name": product.name, "price": product.price,"description": product.description}
   item.append(itemreques)
   return {"message": "Product created successfully", "product": itemreques.get('name')}

@app.get("/products/all")
def get_all_products():
    if item:
        return item
    else:
       raise HTTPException(status_code=404, detail="No products found")



app.include_router(user_router)