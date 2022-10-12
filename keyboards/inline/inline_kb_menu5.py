from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

ikb_menu5=InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='📊Not done yet', callback_data='📊Not done yet')
                                    ]
                                ])