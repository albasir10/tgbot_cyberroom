from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from keyboard import client_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import sqlite_db


class FSMClient(StatesGroup):
    begin = State()
    info_ufa = State()
    info_dema = State()
    client_info = State()
    client_register = State()


# обычный старт который вызывается командой /start
async def command_start(callback: types.CallbackQuery, state: FSMContext):
    try:
        info_user = await sqlite_db.sql_get_info(callback.from_user.id)
        id = callback.from_user.id
        name = callback.from_user.first_name
        if info_user is None:
            await sqlite_db.sql_add_client(id, name)
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_start(answer_kb)
        await bot.send_message(callback.from_user.id,
                               'Привет! О каком клубе хочешь узнать? Выбирай вариант снизу. Если не работают кнопки, напишите что нибудь в чат, бот заговорит с вами вновь',
                               reply_markup=answer_kb)
        await FSMClient.begin.set()
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_start')


# старт после набора любого текста, не для меню
async def command_start_after_message_client(message: types.Message, state: FSMContext):
    try:
        info_user = await sqlite_db.sql_get_info(message.from_user.id)
        id = message.from_user.id
        name = message.from_user.first_name
        if info_user is None:
            await sqlite_db.sql_add_client(id, name)
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_start(answer_kb)
        await bot.send_message(message.from_user.id,
                               'Привет! О каком клубе хочешь узнать? Выбирай вариант снизу. Если не работают кнопки, напишите что нибудь в чат, бот заговорит с вами вновь',
                               reply_markup=answer_kb)
        await FSMClient.begin.set()
    except:
        await message.answer('Общение через лс')
        print('Не получилось отправить сообщение command_start_after_message_client')


# возвращение из любого окна в меню
async def command_start_if_back(callbackmsgcht: types.chat, state: FSMContext):
    try:

        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_start(answer_kb)
        await bot.send_message(callbackmsgcht.id,
                               'О каком клубе хочешь узнать? Выбирай вариант снизу. Если не работают кнопки, напишите что нибудь в чат, бот заговорит с вами вновь',
                               reply_markup=answer_kb)
        await FSMClient.begin.set()
    except:
        await bot.send_message(callbackmsgcht.id, 'Общение через лс')
        print('Не получилось отправить сообщение command_start_if_back')


# выбор инфы уфа
async def command_change_info_ufa(callback: types.CallbackQuery, state: FSMContext):
    try:
        await FSMClient.info_ufa.set()
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_change_info_ufa(answer_kb)
        await bot.send_message(callback.from_user.id,
                               'Выбирай:', reply_markup=answer_kb)
        await callback.answer('')
    except:
        await callback.answer('Ошибка')
        print('Не получилось отправить сообщение command_change_info_ufa')


# инфа о пк в уфа
async def command_change_info_ufa_pc(callback: types.CallbackQuery, state: FSMContext):
    try:
        k = ""
        with open('texts/info_pc_Ufa.txt', encoding='utf-8') as file:
            for item in file:
                k += item
        await bot.send_message(callback.from_user.id, k)
        file.close()
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_pc ')


# акции в уфа
async def command_change_info_ufa_stocks(callback: types.CallbackQuery, state: FSMContext):
    try:
        k = ""
        with open('texts/stocks_Ufa.txt', encoding='utf-8') as file:
            for item in file:
                k += item
        await bot.send_message(callback.from_user.id, k)
        file.close()
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_stocks')


# цены на пк, ps уфа
async def command_change_info_ufa_prices(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/price_ufa.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="цены на пк и ps")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_prices')


# цены на еду уфа
async def command_change_info_ufa_prices_food(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/price_food_ufa.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="цены на еду")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_prices_food')


# игры уфа
async def command_change_info_ufa_games(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/games.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="наши игры")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_games')


# контактная информация в уфа
async def command_change_info_ufa_contacts(callback: types.CallbackQuery, state: FSMContext):
    try:
        k = ""
        with open('texts/contacts_Ufa.txt', encoding='utf-8') as file:
            for item in file:
                k += item
        await bot.send_message(callback.from_user.id, k)
        file.close()
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_contacts')


# --------------------------

# выбор инфы Дема
async def command_change_info_dema(callback: types.CallbackQuery, state: FSMContext):
    try:
        await FSMClient.info_dema.set()
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_change_info_dema(answer_kb)
        await bot.send_message(callback.from_user.id,
                               'Выбирай:', reply_markup=answer_kb)
        await callback.answer('')
    except:
        await callback.answer('Ошибка')
        print('Не получилось отправить сообщение command_change_info_ufa')


# инфа о пк в дема
async def command_change_info_dema_pc(callback: types.CallbackQuery, state: FSMContext):
    try:
        k = ""
        with open('texts/info_pc_Dema.txt', encoding='utf-8') as file:
            for item in file:
                k += item
        await bot.send_message(callback.from_user.id, k)
        file.close()
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_dema_pc ')


# акции в Деме
async def command_change_info_dema_stocks(callback: types.CallbackQuery, state: FSMContext):
    try:
        k = ""
        with open('texts/stocks_Dema.txt', encoding='utf-8') as file:
            for item in file:
                k += item
        await bot.send_message(callback.from_user.id, k)
        file.close()
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_stocks')


# цены на пк, ps Дема
async def command_change_info_dema_prices(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/price_dema.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="цены на пк и ps")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_prices')


# цены на еду Дема
async def command_change_info_dema_prices_food(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/price_food_dema.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="цены на еду")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_prices')


# игры Дема
async def command_change_info_dema_games(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/games.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="наши игры")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_prices')


# Клиенты


# рассылка

async def writing_clients(password: str):
    clients_for_mail = await sqlite_db.sql_get_all_users()
    try:
        text_for_clients = "Привет! Хочешь получить 1 час бесплатно? Держи промокод: " + password + "\nПодойдите к стойке администрации для активации. Код активируется, лишь, для первого показавшего."
        for i in clients_for_mail:
            await bot.send_message(i[0], text_for_clients)
    except:
        print("error ", writing_clients)


# контактная информация в Деме
async def command_change_info_dema_contacts(callback: types.CallbackQuery, state: FSMContext):
    try:
        k = ""
        with open('texts/contacts_Dema.txt', encoding='utf-8') as file:
            for item in file:
                k += item
        await bot.send_message(callback.from_user.id, k)
        file.close()
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_stocks')


# регистрация клиента
async def client_register(callback: types.CallbackQuery, state: FSMContext):
    check_create_user = await sqlite_db.sql_add_client(callback.from_user.id, callback.from_user.username)
    if check_create_user == 1:
        await bot.send_message(callback.from_user.id, 'Регистрация завершена')
        await command_start_if_back(callback.message.chat, state)
    else:
        await bot.send_message(callback.from_user.id, 'Вы не смогли зарегестрироваться, попробуйте позже')
        await command_start_if_back(callback.message.chat, state)


# Ответ на любое сообщение без команды
async def default_message_handler(message: types.Message, state: FSMContext):
    await command_start_after_message_client(message, state)


# Возврат в меню
async def cansel_handler(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.answer("Возврат в начальное меню")
    await command_start_if_back(callback.message.chat, state)


def register_handlers_client(dp: Dispatcher) -> object:
    dp.register_callback_query_handler(cansel_handler, text='отмена', state="*")
    dp.register_callback_query_handler(cansel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_callback_query_handler(command_start, text='start', state=None)
    # раздел инфы о клиенте
    dp.register_callback_query_handler(cansel_handler, text='kb_registration_off', state=FSMClient.client_register)
    dp.register_callback_query_handler(client_register, text='kb_registration_on', state=FSMClient.client_register)
    # раздел инфы о уфе
    dp.register_callback_query_handler(command_change_info_ufa, text='kb_info_ufa', state=FSMClient.begin)
    dp.register_callback_query_handler(command_change_info_ufa_pc, text='kb_info_ufa_pc', state=FSMClient.info_ufa)
    dp.register_callback_query_handler(command_change_info_ufa_stocks, text='kb_info_ufa_stocks',
                                       state=FSMClient.info_ufa)
    dp.register_callback_query_handler(command_change_info_ufa_prices, text='kb_info_ufa_prices',
                                       state=FSMClient.info_ufa)
    dp.register_callback_query_handler(command_change_info_ufa_prices_food, text='kb_info_ufa_prices_food',
                                       state=FSMClient.info_ufa)
    dp.register_callback_query_handler(command_change_info_ufa_games, text='kb_info_ufa_games',
                                       state=FSMClient.info_ufa)
    dp.register_callback_query_handler(command_change_info_ufa_contacts, text='kb_info_ufa_contacts',
                                       state=FSMClient.info_ufa)
    # раздел инфы о деме
    dp.register_callback_query_handler(command_change_info_dema, text='kb_info_dema', state=FSMClient.begin)
    dp.register_callback_query_handler(command_change_info_dema_pc, text='kb_info_dema_pc', state=FSMClient.info_dema)
    dp.register_callback_query_handler(command_change_info_dema_stocks, text='kb_info_dema_stocks',
                                       state=FSMClient.info_dema)
    dp.register_callback_query_handler(command_change_info_dema_prices, text='kb_info_dema_prices',
                                       state=FSMClient.info_dema)
    dp.register_callback_query_handler(command_change_info_dema_prices_food, text='kb_info_dema_prices_food',
                                       state=FSMClient.info_dema)
    dp.register_callback_query_handler(command_change_info_dema_games, text='kb_info_dema_games',
                                       state=FSMClient.info_dema)
    dp.register_callback_query_handler(command_change_info_dema_contacts, text='kb_info_dema_contacts',
                                       state=FSMClient.info_dema)
    # пустой ввод
    dp.register_message_handler(default_message_handler, commands=None, state=None)
