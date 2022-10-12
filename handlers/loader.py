from aiogram import Dispatcher,types,Bot
from handlers import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot = Bot(token=config.BOT_TOKENN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)