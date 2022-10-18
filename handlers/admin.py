from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types


class FSMAdmin(StatesGroup):
    begin = State()


