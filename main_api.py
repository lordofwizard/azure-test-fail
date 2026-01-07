from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory storage
users = {}
items = {}
user_id_counter = 1
item_id_counter = 1


class User(BaseModel):
    name: str
    email: str
    age: int


class Item(BaseModel):
    name: str
    description: str
    price: float


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/users")
def create_user(user: User):
    global user_id_counter
    user_id = user_id_counter
    users[user_id] = user.dict()
    user_id_counter += 1
    return {"id": user_id, **user.dict()}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **users[user_id]}


@app.get("/users")
def list_users():
    return [{"id": uid, **user} for uid, user in users.items()]


@app.post("/items")
def create_item(item: Item):
    global item_id_counter
    item_id = item_id_counter
    items[item_id] = item.dict()
    item_id_counter += 1
    return {"id": item_id, **item.dict()}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items[item_id]}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}
