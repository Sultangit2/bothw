from aiogram import Dispatcher, types
from .loader import download_audio
async def mem(message: types.message):
    if "youtube.com" in message.text:
        await message.answer("Loading...")
        video = open(download_audio(message.text), "rb")
        await message.answer_audio(video)


async def pin_handler(message: types.Message):
    if message.reply_to_message:
        message_to_pin = message.reply_to_message
        await message_to_pin.pin()
        await message.answer("Сообщение закреплено!")
    else:
        await message.answer("Воспользуйся этой командой что бы закрепить сообщение.")


def register_hadlers_extra(dp: Dispatcher):
    dp.register_message_handler(pin_handler, commands=['pin'],commands_prefix='!/')
    dp.register_message_handler(mem, commands=['mem'])