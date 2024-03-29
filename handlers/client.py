from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.client_ufa_commands import menu_and_info_ufa, menu_for_clients_ufa
from handlers.general_commands import start_commands, cansel_commands
from handlers.client_dema_commands import menu_and_info_dema
from handlers.client_ufa_commands.reservation import reservation_menu_ufa
from pay.pay_reservation import pay_for_reservation
from aiogram.types import ContentTypes


class FSMClient(StatesGroup):
    begin = State()
    info_ufa = State()
    info_dema = State()
    menu_ufa = State()
    menu_dema = State()
    reservation_begin_ufa = State()  # вкл когда нажали функцию забронировать
    reservation_choise_pc_ufa = State()  # вкл когда выбрали пк
    reservation_choise_data_ufa = State()  # вкл когда выбрали дату
    reservation_write_number_ufa = State()
    reservation_write_note_ufa = State()
    reservation_write_duration_ufa = State()
    reservation_begin_pay_ufa = State()


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

    reservation_menu_ufa.register_handlers_client(dp)
    dp.register_message_handler(reservation_menu_ufa.reservation_pc_choise_data,
                                commands=None,
                                state=FSMClient.reservation_choise_pc_ufa)

    dp.register_message_handler(reservation_menu_ufa.reservation_pc_write_number,
                                commands=None,
                                state=FSMClient.reservation_choise_data_ufa)

    dp.register_message_handler(reservation_menu_ufa.reservation_pc_write_note,
                                commands=None,
                                state=FSMClient.reservation_write_number_ufa)

    dp.register_message_handler(reservation_menu_ufa.reservation_pc_write_duration,
                                commands=None,
                                state=FSMClient.reservation_write_note_ufa)

    dp.register_callback_query_handler(pay_for_reservation.reservation_pc_give_pay,
                                       text='kb_pay_reservation', state=FSMClient.reservation_write_duration_ufa)

    dp.register_pre_checkout_query_handler(pay_for_reservation.process_pre_checkout_query,
                                           lambda query: True,
                                           state=FSMClient.reservation_begin_pay_ufa)

    dp.register_message_handler(pay_for_reservation.process_successful_payment,
                                content_types=ContentTypes.SUCCESSFUL_PAYMENT,
                                state=FSMClient.reservation_begin_pay_ufa)

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
