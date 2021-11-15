import json
from typing import List
import modules.recommend as rc
from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel 

app = FastAPI()

class Book(BaseModel):
    id: str
    name: str
    tags: list

@app.get("/")
async def root():
    return {"Hello" : "World"}

@app.get("/tag/{qstring}")
async def read_tag(qstring: str):
    return rc.searchTag(qstring)
    raise HTTPException (
        status_code=404, detail=f'Item not found'
    )

@app.get("/book/{qstring}")
async def read_book(qstring: str):
    return rc.searchName(qstring)
    raise HTTPException (
        status_code=404, detail=f'Item not found'
    )

@app.post("/recommend")
async def add_menu(tags: List, books:List):
    return rc.recommend(tags,books)
    raise HTTPException (
        status_code=404, detail=f'Item not found'
    )