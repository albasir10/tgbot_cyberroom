from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboard import client_kb
from handlers import client
from create_bot import bot
from handlers.general_commands import start_commands
from gizmo import connect_gizmo
from data_base import sqlite_db
from generate_text import generate_qr_code


# меню клиентов тцб

async def get_menu_for_client_ufa(callback: types.CallbackQuery, state: FSMContext):
    try:
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_choise_menu_ufa(answer_kb)
        await bot.send_message(callback.from_user.id,
                               'Выбирай:',
                               reply_markup=answer_kb)
        await client.FSMClient.menu_ufa.set()
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
        await start_commands.command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


# Забронировать

async def create_reservation_pc(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:menu_ufa":
        await client.FSMClient.reservation_begin_ufa.set()
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
        await client.FSMClient.reservation_choise_pc_ufa.set()
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
        await client.FSMClient.reservation_choise_data_ufa.set()
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
    if current_state == "FSMClient:reservation_choise_data_ufa":
        await client.FSMClient.reservation_write_number_ufa.set()
        # status_pc_str = await connect_gizmo.create_reservation_pc("ufa")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_cansel(answer_kb)
        await bot.send_message(callback.from_user.id, "Здесь можете вписать комментарий к бронированию, если комментарий не нужен, отправьте любое сообщение:",
                               reply_markup=answer_kb)
        # await state.finish()
        await callback.answer('')
        # await command_start_if_back(callback.message.chat, state)
    else:
        print()  # dema


async def reservation_pc_write_note(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_write_number_ufa":
        await client.FSMClient.reservation_choise_data_ufa.set()
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
        await client.FSMClient.reservation_choise_data_ufa.set()
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

