from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


inventory = {
    1: {
        "name":"milk",
        "price": 5.22,
        "brand": "DoMilk"
    },
    2: {
        "name": "Mass",
        "price": 6.0
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="This is the integer that describes the JSON main object you are looking for")):
    return inventory[item_id]

@app.get("/get-by-name")
def get_by_name(name:str):
    for i in inventory:
        if inventory[i]["name"] == name:
            return inventory[i]
    return "Invalid request"


@app.post("/create-item/{item_id}")
def create_item(item_id:int, item: Item):
    if item_id in inventory:
        return "ERROR: Item already exists"
    else:
        inventory[item_id] = item
        return inventory[item_id]