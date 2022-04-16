from fastapi import APIRouter, Request
from schema import EventObjectModel

router = APIRouter()


@router.post("/consumer/")
async def login(event: EventObjectModel, request: Request):

    data = await request.json()
    data
