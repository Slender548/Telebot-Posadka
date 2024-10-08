from app.utils import get_response, parse_image
from aiogram.types import Message, FSInputFile
from aiogram import Router

router = Router(name="echo")


@router.message()
async def echo_message(message: Message):
    # try:
        response = get_response(message.text)
        text = message.text.replace(",", ".").split("\n")
        if len(text) != 5:
            await message.answer("Нужно ввести 5 значений")
            raise ValueError("Invalid input")
        parse_image(*text)
        await message.answer_photo(FSInputFile("svg_output.png"), caption=response)
    # except:
        # await message.answer("Напишите /help для инструкции")