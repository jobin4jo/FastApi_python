from fastapi import FastAPI
from pydantic import BaseModel

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
@app.get("/products/{product_id}")
def product(product_id: int):
    return {
        "id": product_id,
        "name": f"Product {product_id}",
        "price": 10.0 * product_id
    }

class Product(BaseModel):
    name: str
    price: float
    description: str = None
@app.post("/products/new")
def create_product(product: Product):
   itemreques= {"id":product.id, "name": product.name, "price": product.price}
   item.append(itemreques)
   return {"message": "Product created successfully", "product": itemreques.id}

    