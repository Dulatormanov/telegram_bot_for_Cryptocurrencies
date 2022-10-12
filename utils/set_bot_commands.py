from aiogram import types
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить код'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('register', 'Регистрация'),
        types.BotCommand('menu','Меню')
    ])