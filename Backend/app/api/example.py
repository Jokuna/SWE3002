from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from typing import List

router = APIRouter(
    prefix="/backend/example",
    tags=["example"]
)

@router.get("/", response_class=PlainTextResponse)
async def hello():
    return "Hello World"

@router.get("/{item_id}")
def read_item(item_id: int, q: str = None):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="Invalid item_id")
    return {"item_id": item_id, "q": q}