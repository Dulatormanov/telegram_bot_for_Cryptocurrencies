import logging
from aiogram import Dispatcher
from handlers.config import admins
async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text='Бот Запущен'
            await dp.bot.send_message(chat_id=admin,text=text)
        except Exception as err:
            logging.exception(err)