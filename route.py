from aiogram import Bot
from fastapi import APIRouter, Depends
from schema import EventObjectModel
from bot import init_bot, CHAT_ID
from processing import ProcessingEvent

router = APIRouter()


@router.post("/consumer/")
async def login(
    event: EventObjectModel,
    bot: Bot = Depends(init_bot),
):
    processing = ProcessingEvent(event)
    if processing.is_processed:
        await bot.send_message(
            chat_id=CHAT_ID, text=processing.message, parse_mode="HTML"
        )
