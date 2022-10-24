from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from client_ufa_commands import menu_and_info_ufa, menu_for_clients_ufa
from general_commands import start_commands, cansel_commands
from client_dema_commands import menu_and_info_dema


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


def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(cansel_commands.cansel_handler, text='cansel', state="*")
    dp.register_callback_query_handler(cansel_commands.cansel_handler, Text(equals='отмена', ignore_case=True),
                                       state="*")
    dp.register_callback_query_handler(start_commands.command_start_type_callback, text='start', state=None)
    # раздел инфы о уфе
    dp.register_callback_query_handler(menu_and_info_ufa.command_change_info_ufa, text='kb_info_ufa', state="*")
    dp.register_callback_query_handler(menu_and_info_ufa.command_choice_info_ufa_pc, text='kb_info_ufa_pc', state="*")
    dp.register_callback_query_handler(menu_and_info_ufa.command_choice_info_ufa_stocks, text='kb_info_ufa_stocks',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_ufa.command_choice_info_ufa_prices, text='kb_info_ufa_prices',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_ufa.command_choice_info_ufa_prices_food,
                                       text='kb_info_ufa_prices_food',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_ufa.command_choice_info_ufa_games, text='kb_info_ufa_games',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_ufa.command_choice_info_ufa_contacts, text='kb_info_ufa_contacts',
                                       state="*")
    # раздел меню для уфы
    dp.register_callback_query_handler(menu_for_clients_ufa.get_menu_for_client_ufa, text='kb_menu_ufa', state="*")
    # раздел статус пк для Уфы
    dp.register_callback_query_handler(menu_for_clients_ufa.get_status_pc_info, text='kb_status_pc_now_ufa',
                                       state=FSMClient.menu_ufa)
    # раздел брони для Уфы
    dp.register_callback_query_handler(menu_for_clients_ufa.create_reservation_pc, text='kb_reservation_pc_ufa',
                                       state=FSMClient.menu_ufa)
    # раздел инфы о деме
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema, text='kb_info_dema', state="*")
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema_pc, text='kb_info_dema_pc',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema_stocks, text='kb_info_dema_stocks',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema_prices, text='kb_info_dema_prices',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema_prices_food,
                                       text='kb_info_dema_prices_food',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema_games, text='kb_info_dema_games',
                                       state="*")
    dp.register_callback_query_handler(menu_and_info_dema.command_choice_info_dema_contacts,
                                       text='kb_info_dema_contacts',
                                       state="*")
    # пустой ввод
    dp.register_message_handler(start_commands.default_message_handler, commands=None, state=None)
