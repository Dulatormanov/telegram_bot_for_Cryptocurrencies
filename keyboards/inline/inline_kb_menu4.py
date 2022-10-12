from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu4=InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📊Нур-султан', callback_data='📊Нур-султан'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Алматы', callback_data='📊Алматы'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Шымкент', callback_data='📊Шымкент'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='📊Другой город', callback_data='📊Другой город')
                                    ]
                                ])