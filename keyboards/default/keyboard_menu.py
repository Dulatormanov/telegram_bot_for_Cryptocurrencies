from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_menu=ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Полностью согласен'),
        ],
        [
            KeyboardButton(text='Отказываюсь'),
        ]

    ],
    resize_keyboard=True
)