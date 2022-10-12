from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu=InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Русский', callback_data='Русский'),
                                        InlineKeyboardButton(text='English', callback_data='Английская версия')
                                    ]
                                ])