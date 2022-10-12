from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu6=InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📊Все сделки', callback_data='📊Все сделки'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Выбрать город', callback_data='📊Выбрать город')
                                    ]
                                ])