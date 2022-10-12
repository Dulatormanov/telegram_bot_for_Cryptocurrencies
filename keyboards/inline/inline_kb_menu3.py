from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu3=InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📊Создать сделку', callback_data='📊Создать сделку'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Удалить сделку', callback_data='📊Удалить сделку')
                                    ],
                                    [
                                    InlineKeyboardButton(text='📊История сделок', callback_data='📊История сделок')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Назад', callback_data='Назад')
                                    ]
                                ])