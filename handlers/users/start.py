from aiogram import types
from handlers.loader import dp
from keyboards.default import kb_menu,kb_menu2
from keyboards.inline import ikb_menu, ikb_menu2, ikb_menu3, ikb_menu4,ikb_menu5,ikb_menu6
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command
@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer('Вы подтверждаете,'
                         'что ознакомились'
                         '  и согласны с'
                         '    условиями  '
                         '  предостваления'
                         '      услуг?', reply_markup=kb_menu)
@dp.message_handler(text='Полностью согласен')
async def command_star(message: types.Message):
    await message.answer('🌐Язык\n'
                         'Выберите язык\n'
                         ' интерфейса.', reply_markup=ikb_menu)
@dp.callback_query_handler(text='Русский')
async def command_sta(call: CallbackQuery):
    await call.message.answer(f'Приветствую, {call.message.from_user.full_name}\n'
                      f'Это телеграм бот криптоплатформы'
                      f'Crypto Bankroll https://www.google.com/ для обмена'
                      f'криптовалюты Tether(USDT) и'
                      f'        фиатных денег.',reply_markup=kb_menu2)
@dp.message_handler(text='📊Обмен USDT/USD')
async def command_st(message: types.Message):
    await message.answer('            Обмен USDT/USD\n\n'
                         'Здесь Вы совершаете сделки с людьми, а бот'
                         '           выступает как гарант.\n'
                         '  Вы находитесь в безопасном режиме. Его'
                         'можно отключить после проведения 2х сделок.\n'
                         ' Напоминаем, что все комиссии должны быть'
                         '    включены в курс, покупатель должен'
                         '  отправлять точную сумму, как указано в '
                         '                 сделке!\n'
                         'В случае нарушения данного правила, просим'
                         '      сообщить в службу поддержки', reply_markup=ikb_menu2)
@dp.callback_query_handler(text='📊Мои сделки')
async def command_s(call: CallbackQuery):
    await call.message.answer('Мои сделки', reply_markup=ikb_menu3)

@dp.callback_query_handler(text='📊Создать сделку')
async def command_t(call: CallbackQuery):
    await call.message.answer('Создать сделку', reply_markup=ikb_menu4)


@dp.callback_query_handler(text='📊Удалить сделку')
async def command_tr(call: CallbackQuery):
    await call.message.answer('Удалить сделку', reply_markup=ikb_menu5)


@dp.callback_query_handler(text='📊Список сделок')
async def command_tre(call: CallbackQuery):
    await call.message.answer('📊Список сделок',reply_markup=ikb_menu6)


@dp.callback_query_handler(text='📊Все сделки')
async def command_tree(call: CallbackQuery):
    await call.message.answer('Все сделки')


@dp.callback_query_handler(text='📊Выбрать город')
async def command_tre(call: CallbackQuery):
    await call.message.answer('📊Выбрать город', reply_markup=ikb_menu4)