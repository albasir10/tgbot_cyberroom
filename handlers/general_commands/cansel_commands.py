from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from data_base import sqlite_db
from aiogram.dispatcher import FSMContext
from keyboard import client_kb
from handlers import client
from create_bot import bot
from handlers.general_commands import start_commands


# Возврат в меню
async def cansel_handler(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.answer("Возврат в начальное меню")
    await start_commands.command_start_if_back(callback.message.chat, state)
