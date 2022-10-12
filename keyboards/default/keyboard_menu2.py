from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_menu2=ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='📊Обмен USDT/USD'),
        ],
        [
            KeyboardButton(text='Настройки'),
        ]

    ],
    resize_keyboard=True
)