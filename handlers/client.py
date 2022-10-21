import base64

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot
from keyboard import client_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from data_base import sqlite_db
from generate_text import generate_qr_code
from gizmo import connect_gizmo


class FSMClient(StatesGroup):
    begin = State()
    info_ufa = State()
    info_dema = State()
    menu_ufa = State()
    menu_dema = State()
    reservation_begin_ufa = State()
    reservation_choise_pc_ufa = State()
    reservation_choise_data_ufa = State()
    reservation_write_number_ufa = State()
    reservation_write_note_ufa = State()
    reservation_write_duration_ufa = State()


# обычный старт который вызывается командой /start
async def command_start_type_callback(callback: types.CallbackQuery, state: FSMContext):
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
        await callback.answer('Ошибка')
        print('Не получилось отправить сообщение command_start_type_callback')


# старт после набора любого текста, не для меню
async def command_start_type_message(message: types.Message, state: FSMContext):
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
        await message.answer('ООшибка')
        print('Не получилось отправить сообщение command_start_type_message')


# возвращение из любого окна в меню
async def command_start_if_back(callback_message_chat: types.chat, state: FSMContext):
    try:
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_start(answer_kb)
        await bot.send_message(callback_message_chat.id,
                               'О каком клубе хочешь узнать? Выбирай вариант снизу. Если не работают кнопки, напишите что нибудь в чат, бот заговорит с вами вновь',
                               reply_markup=answer_kb)
        await FSMClient.begin.set()
    except:
        await bot.send_message(callback_message_chat.id, 'Ошибка')
        print('Не получилось отправить сообщение command_start_if_back')


"""         УФА           """


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
async def command_choice_info_ufa_pc(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_ufa_stocks(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_ufa_prices(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_ufa_prices_food(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_ufa_games(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_ufa_contacts(callback: types.CallbackQuery, state: FSMContext):
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


"""         ДЕМА           """


# выбор инфы Дема
async def command_choice_info_dema(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_dema_pc(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_dema_stocks(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_dema_prices(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_dema_prices_food(callback: types.CallbackQuery, state: FSMContext):
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
async def command_choice_info_dema_games(callback: types.CallbackQuery, state: FSMContext):
    try:
        photo = InputFile("pictures/games.jpg")
        await bot.send_photo(callback.from_user.id, photo=photo, caption="наши игры")
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_prices')


# контактная информация в Деме
async def command_choice_info_dema_contacts(callback: types.CallbackQuery, state: FSMContext):
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


"""         КЛИЕНТЫ          """


# меню клиентов тцб

async def get_menu_for_client_ufa(callback: types.CallbackQuery, state: FSMContext):
    try:
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_choise_menu_ufa(answer_kb)
        await bot.send_message(callback.from_user.id,
                               'Выбирай:',
                               reply_markup=answer_kb)
        await FSMClient.menu_ufa.set()
        await callback.answer('')
    except:
        await callback.answer('Ошибка')
        print('Не получилось отправить сообщение get_menu_for_client')


# статус компов

async def get_status_pc_info(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:menu_ufa":
        status_pc_str = await connect_gizmo.get_all_status_pc("ufa")
        await bot.send_message(callback.from_user.id, status_pc_str)
        await state.finish()
        await callback.answer('')
        await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


# Забронировать

async def create_reservation_pc(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:menu_ufa":
        await FSMClient.reservation_begin_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_choise_pc_for_reservation_ufa(answer_kb)
        await bot.send_message(callback.from_user.id, "Какой пк хотите забронировать?", reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


async def reservation_pc_choise_pc(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_begin_ufa":
        await FSMClient.reservation_choise_pc_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_cansel(answer_kb)
        await bot.send_message(callback.from_user.id, "Напишите дату, пример: 2022-10-23T04:25:23.507Z",
                               reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


async def reservation_pc_choise_data(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_choise_pc_ufa":
        await FSMClient.reservation_choise_data_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_cansel(answer_kb)
        await bot.send_message(callback.from_user.id, "Напишите свой номер:",
                               reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


async def reservation_pc_write_number(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_write_number_ufa":
        await FSMClient.reservation_choise_data_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_cansel(answer_kb)
        await bot.send_message(callback.from_user.id, "Напишите свой номер:",
                               reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


async def reservation_pc_write_note(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_write_number_ufa":
        await FSMClient.reservation_choise_data_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_cansel(answer_kb)
        await bot.send_message(callback.from_user.id, "Напишите свой номер:",
                               reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


async def reservation_pc_write_duration(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_write_number_ufa":
        await FSMClient.reservation_choise_data_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_cansel(answer_kb)
        await bot.send_message(callback.from_user.id, "Напишите свой номер:",
                               reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


# рассылка

async def writing_clients(password: str):
    clients_for_mail = await sqlite_db.sql_get_all_users()
    qr_code_bytes = await generate_qr_code.create_qr_code(password)
    try:
        text_for_clients = "📪 Привет! Хотите получить 1 час бесплатно? Берите QR код!\nПодойдите к стойке администрации для активации. Код активируется, лишь, для первого показавшего."
        for i in clients_for_mail:
            await bot.send_photo(i[0], photo=qr_code_bytes, caption=text_for_clients)
    except:
        print("error ", writing_clients)


"""         ОБЩЕЕ           """


# Ответ на любое сообщение без команды
async def default_message_handler(message: types.Message, state: FSMContext):
    await command_start_type_message(message, state)


# Возврат в меню
async def cansel_handler(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.answer("Возврат в начальное меню")
    await command_start_if_back(callback.message.chat, state)


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(cansel_handler, text='cansel', state="*")
    dp.register_callback_query_handler(cansel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_callback_query_handler(command_start_type_callback, text='start', state=None)
    # раздел инфы о уфе
    dp.register_callback_query_handler(command_change_info_ufa, text='kb_info_ufa', state="*")
    dp.register_callback_query_handler(command_choice_info_ufa_pc, text='kb_info_ufa_pc', state="*")
    dp.register_callback_query_handler(command_choice_info_ufa_stocks, text='kb_info_ufa_stocks',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_ufa_prices, text='kb_info_ufa_prices',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_ufa_prices_food, text='kb_info_ufa_prices_food',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_ufa_games, text='kb_info_ufa_games',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_ufa_contacts, text='kb_info_ufa_contacts',
                                       state="*")
    # раздел меню для уфы
    dp.register_callback_query_handler(get_menu_for_client_ufa, text='kb_menu_ufa', state="*")
    # раздел статус пк для Уфы
    dp.register_callback_query_handler(get_status_pc_info, text='kb_status_pc_now_ufa', state=FSMClient.menu_ufa)
    # раздел брони для Уфы
    dp.register_callback_query_handler(create_reservation_pc, text='kb_reservation_pc_ufa', state=FSMClient.menu_ufa)
    # раздел инфы о деме
    dp.register_callback_query_handler(command_choice_info_dema, text='kb_info_dema', state="*")
    dp.register_callback_query_handler(command_choice_info_dema_pc, text='kb_info_dema_pc', state="*")
    dp.register_callback_query_handler(command_choice_info_dema_stocks, text='kb_info_dema_stocks',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_dema_prices, text='kb_info_dema_prices',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_dema_prices_food, text='kb_info_dema_prices_food',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_dema_games, text='kb_info_dema_games',
                                       state="*")
    dp.register_callback_query_handler(command_choice_info_dema_contacts, text='kb_info_dema_contacts',
                                       state="*")
    # пустой ввод
    dp.register_message_handler(default_message_handler, commands=None, state=None)
