from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

a1 = InlineKeyboardButton(text='1', callback_data='1')
kb_inline = InlineKeyboardMarkup(row_width=2).add(a1)


async def answer_start(kb_inline):
    a1 = InlineKeyboardButton(text='Информация ТЦБ', callback_data='kb_info_ufa')
    a2 = InlineKeyboardButton(text='Информация Дема', callback_data='kb_info_dema')
    kb_inline = InlineKeyboardMarkup(row_width=2).add(a1).add(a2)
    return kb_inline


async def answer_change_info_ufa(kb_inline):
    a1 = InlineKeyboardButton(text='информация о пк', callback_data='kb_info_ufa_pc')
    a2 = InlineKeyboardButton(text='акции', callback_data='kb_info_ufa_stocks')
    a3 = InlineKeyboardButton(text='цены на пк, ps', callback_data='kb_info_ufa_prices')
    a4 = InlineKeyboardButton(text='цены на еду', callback_data='kb_info_ufa_prices_food')
    a5 = InlineKeyboardButton(text='доступные игры', callback_data='kb_info_ufa_games')
    a6 = InlineKeyboardButton(text='контактная информация', callback_data='kb_info_ufa_contacts')
    kb_inline = InlineKeyboardMarkup(row_width=2).add(a1).add(a2).add(a3).add(a4).add(a5).add(a6)
    return kb_inline


async def answer_change_info_dema(kb_inline):
    a1 = InlineKeyboardButton(text='информация о пк', callback_data='kb_info_dema_pc')
    a2 = InlineKeyboardButton(text='акции', callback_data='kb_info_dema_stocks')
    a3 = InlineKeyboardButton(text='цены на пк, ps', callback_data='kb_info_dema_prices')
    a4 = InlineKeyboardButton(text='цены на еду', callback_data='kb_info_dema_prices_food')
    a5 = InlineKeyboardButton(text='доступные игры', callback_data='kb_info_dema_games')
    a6 = InlineKeyboardButton(text='контактная информация', callback_data='kb_info_dema_contacts')
    kb_inline = InlineKeyboardMarkup(row_width=2).add(a1).add(a2).add(a3).add(a4).add(a5).add(a6)
    return kb_inline
