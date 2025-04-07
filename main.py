from fastapi import FastAPI

app= FastAPI()

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

    