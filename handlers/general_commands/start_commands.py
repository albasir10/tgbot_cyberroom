from aiogram.types import InlineKeyboardMarkup
from aiogram import types
from data_base import sqlite_db
from aiogram.dispatcher import FSMContext
from keyboard import client_kb
from handlers import client
from create_bot import bot


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
        await client.FSMClient.begin.set()
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
        await client.FSMClient.begin.set()
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
        await client.FSMClient.begin.set()
    except:
        await bot.send_message(callback_message_chat.id, 'Ошибка')
        print('Не получилось отправить сообщение command_start_if_back')


# Ответ на любое сообщение без команды
async def default_message_handler(message: types.Message, state: FSMContext):
    await command_start_type_message(message, state)