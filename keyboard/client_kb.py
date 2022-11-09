from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

a1 = InlineKeyboardButton(text='1', callback_data='1')
kb_inline = InlineKeyboardMarkup(row_width=2).add(a1)


async def answer_start(kb_inline):
    a1 = InlineKeyboardButton(text='📜 Информация ТЦБ', callback_data='kb_info_ufa')
    a2 = InlineKeyboardButton(text='📜 Информация Дема', callback_data='kb_info_dema')
    a3 = InlineKeyboardButton(text='🔮 Для клиентов ТЦБ', callback_data='kb_menu_ufa')
    a4 = InlineKeyboardButton(text='💎 Для клиентов Дема', callback_data='kb_menu_dema')
    kb_inline = InlineKeyboardMarkup(row_width=2).row(a1, a2).row(a3, a4)
    return kb_inline


async def answer_cansel(kb_inline):
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup().add(back)
    return kb_inline


async def answer_choise_menu_ufa(kb_inline):
    # a1 = InlineKeyboardButton(text='🖥 статус пк', callback_data='kb_status_pc_now_ufa')
    a2 = InlineKeyboardButton(text='🗄 забронировать пк', callback_data='kb_reservation_pc_ufa')
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup(row_width=2).row(a2).add(back)
    return kb_inline


async def answer_choise_pc_for_reservation_ufa(kb_inline):
    pc1 = InlineKeyboardButton(text='🥉 Premium 1', callback_data='kb_choise_reservation_pc_ufa_1')
    pc2 = InlineKeyboardButton(text='🥉 Premium 2', callback_data='kb_choise_reservation_pc_ufa_2')
    pc3 = InlineKeyboardButton(text='🥉 Premium 3', callback_data='kb_choise_reservation_pc_ufa_3')
    pc4 = InlineKeyboardButton(text='🥉 Premium 4', callback_data='kb_choise_reservation_pc_ufa_4')
    pc5 = InlineKeyboardButton(text='🥉 Premium 5', callback_data='kb_choise_reservation_pc_ufa_5')
    pc6 = InlineKeyboardButton(text='🥉 Premium 6', callback_data='kb_choise_reservation_pc_ufa_6')
    pc7 = InlineKeyboardButton(text='🥉 Premium 7', callback_data='kb_choise_reservation_pc_ufa_7')
    pc8 = InlineKeyboardButton(text='🥉 Premium 8', callback_data='kb_choise_reservation_pc_ufa_8')
    pc9 = InlineKeyboardButton(text='🥉 Premium 9', callback_data='kb_choise_reservation_pc_ufa_9')
    pc10 = InlineKeyboardButton(text='🥉 Premium 10', callback_data='kb_choise_reservation_pc_ufa_10')
    pc11 = InlineKeyboardButton(text='🥈 Bootcamp 11', callback_data='kb_choise_reservation_pc_ufa_11')
    pc12 = InlineKeyboardButton(text='🥈 Bootcamp 12', callback_data='kb_choise_reservation_pc_ufa_12')
    pc13 = InlineKeyboardButton(text='🥈 Bootcamp 13', callback_data='kb_choise_reservation_pc_ufa_13')
    pc14 = InlineKeyboardButton(text='🥈 Bootcamp 14', callback_data='kb_choise_reservation_pc_ufa_14')
    pc15 = InlineKeyboardButton(text='🥈 Bootcamp 15', callback_data='kb_choise_reservation_pc_ufa_15')
    pc21 = InlineKeyboardButton(text='🥈 Bootcamp 21', callback_data='kb_choise_reservation_pc_ufa_21')
    pc22 = InlineKeyboardButton(text='🥈 Bootcamp 22', callback_data='kb_choise_reservation_pc_ufa_22')
    pc23 = InlineKeyboardButton(text='🥈 Bootcamp 23', callback_data='kb_choise_reservation_pc_ufa_23')
    pc24 = InlineKeyboardButton(text='🥈 Bootcamp 24', callback_data='kb_choise_reservation_pc_ufa_24')
    pc25 = InlineKeyboardButton(text='🥈 Bootcamp 25', callback_data='kb_choise_reservation_pc_ufa_25')
    pc45 = InlineKeyboardButton(text='🥇 Luxe 45', callback_data='kb_choise_reservation_pc_ufa_45')
    pc46 = InlineKeyboardButton(text='🥇 Luxe 46', callback_data='kb_choise_reservation_pc_ufa_46')
    pc47 = InlineKeyboardButton(text='🥇 Luxe 47', callback_data='kb_choise_reservation_pc_ufa_47')
    pc50 = InlineKeyboardButton(text='🥇 Luxe 50', callback_data='kb_choise_reservation_pc_ufa_50')
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup().row(pc1, pc2).row(pc3, pc4).row(pc5, pc6).row(pc7, pc8) \
        .row(pc9, pc10).row(pc11, pc12).row(pc13, pc14).row(pc15, pc21).row(pc22, pc23).row(pc24, pc25) \
        .row(pc45, pc46).row(pc47, pc50).add(back)
    return kb_inline


async def answer_text_and_back(kb_inline):
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup().add(back)
    return kb_inline


async def answer_pay_reservation_begin(kb_inline):
    pc1 = InlineKeyboardButton(text='Оплатить', callback_data='kb_pay_reservation')
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup().add(pc1).add(back)
    return kb_inline


async def answer_change_info_ufa(kb_inline):
    a1 = InlineKeyboardButton(text='ℹ информация о пк', callback_data='kb_info_ufa_pc')
    a2 = InlineKeyboardButton(text='🎉 акции', callback_data='kb_info_ufa_stocks')
    a3 = InlineKeyboardButton(text='🖥 цены на пк, ps', callback_data='kb_info_ufa_prices')
    a4 = InlineKeyboardButton(text='🎮 доступные игры', callback_data='kb_info_ufa_games')
    a5 = InlineKeyboardButton(text='🍕 цены на еду', callback_data='kb_info_ufa_prices_food')
    a6 = InlineKeyboardButton(text='📞 контакты', callback_data='kb_info_ufa_contacts')
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup(row_width=2).row(a1, a2).row(a3, a4).row(a5, a6).add(back)
    return kb_inline


async def answer_change_info_dema(kb_inline):
    a1 = InlineKeyboardButton(text='ℹ информация о пк', callback_data='kb_info_dema_pc')
    a2 = InlineKeyboardButton(text='🎉 акции', callback_data='kb_info_dema_stocks')
    a3 = InlineKeyboardButton(text='🖥 цены на пк, ps', callback_data='kb_info_dema_prices')
    a4 = InlineKeyboardButton(text='🍕 цены на еду', callback_data='kb_info_dema_prices_food')
    a5 = InlineKeyboardButton(text='🎮 доступные игры', callback_data='kb_info_dema_games')
    a6 = InlineKeyboardButton(text='📞 контакты', callback_data='kb_info_ufa_contacts')
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup(row_width=2).row(a1, a2).row(a3, a4).row(a5, a6).add(back)
    return kb_inline
