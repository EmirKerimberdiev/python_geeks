import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import dotenv_values
import logging

token = dotenv_values(".env")['token']
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_handler(message):
    name = message.from_user.first_name
    await message.answer(f"Добро {name} пожаловать на бот Backend_bot этот бот был создан для практики в качестве бота для меня!")

@dp.message(Command(commands=['pic']))
async def pic_handler(message):
    image = types.FSInputFile('ea97ef2e-793a-4513-ad2c-82d7b340263c.webp')
    await message.answer_photo(image)


@dp.message()
async def echo_handler(message):
    text = message.text
    await message.answer(text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
