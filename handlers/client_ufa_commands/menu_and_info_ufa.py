from aiogram.types import InlineKeyboardMarkup,  InputFile
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboard import client_kb
from handlers import client
from create_bot import bot
from handlers.general_commands import start_commands


# выбор инфы уфа
async def command_change_info_ufa(callback: types.CallbackQuery, state: FSMContext):
    try:
        await client.FSMClient.info_ufa.set()
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
        await start_commands.command_start_if_back(callback.message.chat, state)
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
        await start_commands.command_start_if_back(callback.message.chat, state)
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
        await start_commands.command_start_if_back(callback.message.chat, state)
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
        await start_commands.command_start_if_back(callback.message.chat, state)
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
        await start_commands.command_start_if_back(callback.message.chat, state)
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
        await start_commands.command_start_if_back(callback.message.chat, state)
    except:
        await callback.answer('Общение через лс')
        print('Не получилось отправить сообщение command_change_info_ufa_contacts')
