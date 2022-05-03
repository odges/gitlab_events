import aiohttp
from aiogram import Bot

from environment import TELEGRAM_BOT


async def init_bot() -> Bot:
    return Bot(token=TELEGRAM_BOT)


async def get_groups():
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT}/getUpdates"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_json = await response.json()
            response_json
