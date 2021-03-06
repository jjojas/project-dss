import json
from typing import List
import modules.recommend as rc
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://norecsdss05.netlify.app",
    "https://suspicious-goldwasser-e5c8ea.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    id: str
    name: str
    tags: list

@app.get("/")
async def root():
    return {"Hello" : "World"}

@app.get("/tag/")
async def read_all_tag():
    return rc.AllTag()
    raise HTTPException (
        status_code=404, detail=f'Item not found'
    )

# @app.get("/book/")
# async def read_all_book():
#     return rc.AllBook()
#     raise HTTPException (
#         status_code=404, detail=f'Item not found'
#     )

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
async def get_recommendation(tags: List, books:List):
    return rc.recommend(tags,books)
    raise HTTPException (
        status_code=404, detail=f'Item not found'
    )