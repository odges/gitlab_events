import json

from bot import init_bot
from environment import CHAT_ID
from gitlab_handler.handler import ProcessingEvent
from schema import EventObjectModel
from gitlab_handler.handler_errors import NotImplementedStatus


async def handler(event, context):
    """Yandex handler for cloud function

    Args:
        event: input event from yc
        context: input context from yc

    Returns:
        response: response for yc
    """
    body_request = json.loads(event["body"])

    bot = await init_bot()
    event = EventObjectModel(**body_request)
    try:
        processing = ProcessingEvent(event)
    except NotImplementedStatus as error:
        return {
            "statusCode": 501,
            "body": error.text,
        }
    await bot.send_message(chat_id=CHAT_ID, text=processing.message, parse_mode="HTML")

    return {
        "statusCode": 200,
        "body": "success",
    }
