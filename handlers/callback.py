from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("следущий вопрос?", callback_data="button_2")
    markup.add(button)

    question = "в шахматах сколько клеток?"
    answers = [
        "46",
        "85",
        "55",
        "64",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="стыдно не знать!",
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):

    question = 'кто такой манделла?'
    answers = [
        'хз',
        'врач',
        'космонавт',
        'президент',
        'блогер',
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать(",
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")