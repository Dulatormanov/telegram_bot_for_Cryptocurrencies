from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu2=InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📊Мои сделки', callback_data='📊Мои сделки'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Список сделок', callback_data='📊Список сделок')
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Назад', callback_data='📊Назад')
                                    ]
                                ])