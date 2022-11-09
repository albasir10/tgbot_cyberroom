from aiogram.types import InlineKeyboardMarkup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboard import client_kb
from handlers import client
from create_bot import bot, dp
from gizmo import connect_gizmo
from handlers.general_commands import start_commands


async def reservation_pc_choise_pc(callback: types.CallbackQuery, state: FSMContext):
    await client.FSMClient.reservation_choise_pc_ufa.set()
    number_pc = callback.data[callback.data.rfind('_') + 1:]
    with open("clients_data/create_reservation_data/" + str(callback.from_user.id) + ".txt", 'w', encoding="cp1251") as f:
        f.write("pc=" + number_pc + "\n")
    answer_kb = InlineKeyboardMarkup()
    answer_kb = await client_kb.answer_text_and_back(answer_kb)
    await bot.send_message(callback.from_user.id, "Напишите дату, затем, в какой час придете пример: 09.11.2022 9 "
                                                  "или 09.11.2022 19", reply_markup=answer_kb)
    await callback.answer('')


async def reservation_pc_choise_data(message: types.Message, state: FSMContext):
    await client.FSMClient.reservation_choise_data_ufa.set()
    date_pc = message.text
    if await connect_gizmo.create_reservation_pc_test(message.from_user.id, date_pc):
        with open("clients_data/create_reservation_data/" + str(message.from_user.id) + ".txt", 'a') as f:
            f.write("date=" + date_pc + "\n")
        answer_kb = InlineKeyboardMarkup()
        answer_kb = await client_kb.answer_text_and_back(answer_kb)
        await bot.send_message(message.from_user.id, "Напишите свой номер (начинайте с 8, пример: 89172233025):", reply_markup=answer_kb)
    else:
        await bot.send_message(message.from_user.id,
                               "К сожалению в это время пк будет не доступен.")
        await state.finish()
        await start_commands.command_start_type_message(message, state)


async def reservation_pc_write_number(message: types.Message, state: FSMContext):
    await client.FSMClient.reservation_write_number_ufa.set()
    number_client = message.text
    with open("clients_data/create_reservation_data/" + str(message.from_user.id) + ".txt", 'a', encoding="cp1251") as f:
        f.write("number=" + number_client + "\n")
    answer_kb = InlineKeyboardMarkup()
    answer_kb = await client_kb.answer_text_and_back(answer_kb)
    await bot.send_message(message.from_user.id,
                           "Здесь можете вписать комментарий к бронированию, если комментарий не нужен, отправьте любое сообщение:", reply_markup=answer_kb)


async def reservation_pc_write_note(message: types.Message, state: FSMContext):
    await client.FSMClient.reservation_write_note_ufa.set()
    note_client = message.text
    with open("clients_data/create_reservation_data/" + str(message.from_user.id) + ".txt", 'a') as f:
        f.write("note=" + note_client + "\n")
    answer_kb = InlineKeyboardMarkup()
    answer_kb = await client_kb.answer_text_and_back(answer_kb)
    await bot.send_message(message.from_user.id,
                           "Напишите на сколько часов хотите сесть (нужна только цифра, пример: 5):", reply_markup=answer_kb)


async def reservation_pc_write_duration(message: types.Message, state: FSMContext):
    await client.FSMClient.reservation_write_duration_ufa.set()
    duration_client = message.text
    with open("clients_data/create_reservation_data/" + str(message.from_user.id) + ".txt", 'a') as f:
        f.write("duration=" + duration_client + "\n")
    answer_kb = InlineKeyboardMarkup()
    answer_kb = await client_kb.answer_pay_reservation_begin(answer_kb)
    await bot.send_message(message.from_user.id, "Хорошо, мы получили информацию, теперь нужно внести предоплату",
                           reply_markup=answer_kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_1',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_2',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_3',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_4',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_5',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_6',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_7',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_8',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_9',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_10',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_11',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_12',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_13',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_14',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_15',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_21',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_22',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_23',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_24',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_25',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_45',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_46',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_47',
                                       state=client.FSMClient.reservation_begin_ufa)
    dp.register_callback_query_handler(reservation_pc_choise_pc, text='kb_choise_reservation_pc_ufa_50',
                                       state=client.FSMClient.reservation_begin_ufa)
