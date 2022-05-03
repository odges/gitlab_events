from aiogram import Bot
from fastapi import APIRouter, Depends

from bot import init_bot
from environment import CHAT_ID
from gitlab_handler.handler import ProcessingEvent
from schema import EventObjectModel

router = APIRouter()


@router.post("/consumer/")
async def consumer(
    event: EventObjectModel,
    bot: Bot = Depends(init_bot),
):
    """Consumer for gitlab webhook (https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)

    Args:
        event (EventObjectModel): gitlab event send by gitlab
        bot (Bot, optional): telegam bot
    """
    processing = ProcessingEvent(event)
    await bot.send_message(chat_id=CHAT_ID, text=processing.message, parse_mode="HTML")
