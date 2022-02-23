from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import os

from parser import Parser, URL_MAIL, URL_KUP_LEFT, URL_KUP_RIGHT, URL_GORG

API_TOKEN = '5012311689:AAF_Bx-yr7nXwldwBiYSSI5u9ELK0Joxx3k'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Command('start'))
async def bus_bot(message: types.Message):
    menu = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton('Почта')
            KeyboardButton('Гор-шоссе')
        ],
        [
            KeyboardButton('Новогиреево'),
            KeyboardButton('Первомайская'),
        ],

    ], resize_keyboard=True)
    await message.answer('Куда едем?', reply_markup=menu)


@dp.message_handler(Text(equals=['Почта', 'Новогиреево', 'Первомайская', 'Гор-шоссе']))
async def choice_bus(message: types.Message):
    if message.text == 'Почта':
        parser = Parser(URL_MAIL)
        parser.get_content()
        bus = parser.open_content()
        parser.erase_content()
        await message.answer(bus)
    elif message.text == 'Новогиреево':
        parser = Parser(URL_KUP_LEFT)
        parser.get_content()
        bus = parser.open_content()
        parser.erase_content()
        await message.answer(bus)
    elif message.text == 'Первомайская':
        parser = Parser(URL_KUP_RIGHT)
        parser.get_content()
        bus = parser.open_content()
        parser.erase_content()
        await message.answer(bus)
    elif message.text == 'Гор-шоссе':
        parser = Parser(URL_GORG)
        parser.get_content()
        bus = parser.open_content()
        parser.erase_content()
        await message.answer(bus)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)