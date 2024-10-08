import asyncio
from aiogram import Bot, Dispatcher
# import cairosvg
from app.config import resolve_token
from app.handlers import get_router

API_TOKEN = resolve_token()

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(get_router())

asyncio.get_event_loop().run_until_complete(dp.start_polling(bot))