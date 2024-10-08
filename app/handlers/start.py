from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router(name="start")

@router.message(Command("start", "help"))
async def send_welcome(message: Message):
    await message.reply("""Привет! Пиши в формат 
D=
ES=
EI=
es=
ei=
К примеру:
45
0,039
0
0
-0,039""")


