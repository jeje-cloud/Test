from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def getting_teas():
    return teas

@app.post("/teas/")
def add_tea(item: Item):
    teas.append(item)
    return item

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int, update_tea:Item):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
        
    return {"error: no tea found"}

@app.delete("/teas/{tea_id}")
def deleting_tea(tea_id:int):
    for index,tea in enumerate(teas):
        if tea.id ==  tea_id:
            deleted_tea = teas.pop(index)
            return deleted_tea        

    return {"tea not found"}
    

            
    



    

