from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboard import client_kb
from handlers import client
from create_bot import bot
from handlers.general_commands import start_commands
from gizmo import connect_gizmo


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







