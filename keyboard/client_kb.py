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


async def answer_choise_menu_ufa(kb_inline):
    a1 = InlineKeyboardButton(text='🖥 статус компьютеров', callback_data='kb_status_pc_now_ufa')
    back = InlineKeyboardButton(text='🔙 отмена', callback_data='cansel')
    kb_inline = InlineKeyboardMarkup(row_width=2).row(a1).add(back)
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
