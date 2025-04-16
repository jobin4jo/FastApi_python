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

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    existing_user = db.fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))
    print(existing_user)
    if not existing_user:
        return {"error": "User not found"}
    if user.name == existing_user[1] and user.email == existing_user[2]:
        return {"message": "No changes detected"}
    db.execute_query("UPDATE users SET name = ?, email = ? WHERE id = ?", (user.name, user.email, user_id))
    return {"message": "User updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    existing_user = db.fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))
    if not existing_user:
        return {"error": "User not found"}
    db.execute_query("DELETE FROM users WHERE id = ?", (user_id,))
    return {"message": "User deleted"}