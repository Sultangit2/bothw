from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import Dispatcher, types


async def quiz1(message: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("следущий вопрос?", callback_data="button_1")
    markup.add(button)

    question = "сколько дней до лета?"
    answers = [
        "20",
        "18",
        "27",
        "хз",
    ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="стыдно не знать!",
        open_period=15,
        reply_markup=markup

    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=['quiz'])


