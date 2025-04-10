from fastapi import FastAPI
from pydantic import BaseModel
import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.execute_query('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: User):
    db.execute_query("INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email))
    return {"message": "User created"}

@app.get("/users/")
def get_users():
    return {"users": db.fetch_all("SELECT * FROM users")}
