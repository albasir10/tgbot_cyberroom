import os
from aiogram.types import ContentTypes
from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from handlers import client

token_pay = os.getenv('TOKENPAY')
PRICE = types.LabeledPrice(label='чек', amount=10000)


async def reservation_pc_give_pay(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "FSMClient:reservation_write_duration_ufa":
        await client.FSMClient.reservation_begin_pay_ufa.set()
        await bot.send_invoice(
            callback.from_user.id,
            title='test',
            description='test_descript',
            provider_token='401643678:TEST:a81d59e8-8fb7-480e-ad41-a429e5a9db7a',
            currency='rub',
            is_flexible=False,
            prices=[PRICE],
            payload='check_load_pay'
        )
    else:
        print()  # dema


async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def process_successful_payment(message: types.Message):
    pmnt = message.successful_payment.to_python()
    await bot.send_message(
        message.chat.id, "gg"
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_successful_payment, content_types=ContentTypes.SUCCESSFUL_PAYMENT)
    dp.register_pre_checkout_query_handler(process_pre_checkout_query, lambda query: True)
    dp.register_callback_query_handler(reservation_pc_give_pay, text='kb_pay_reservation',
                                       state=client.FSMClient.reservation_write_duration_ufa)




