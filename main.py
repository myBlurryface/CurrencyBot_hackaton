from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import asyncio
import texts as T
import Keyboards as K
import constants as C
import dicts as DCT
from api_calls import banks_dict, get_file, functions_calls

#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#
bot = Bot(token=C.BOT_API_TOKEN)                                 #
dp = Dispatcher(bot)                                            #
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+#
chat_states = {}
users_currency = {}                                             #
users_banks = {}                                                #
#===============================================================#

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    id = message.chat.id
    users_banks[id] = ''
    users_currency[id] = ''
    keyboard_start = await K.get_bank_keyboard()
    await bot.send_message(id, T.greetings, reply_markup=keyboard_start)


@dp.message_handler(content_types=["text"])
async def handle_text(message: types.Message):
      await bot.send_message(message.chat.id, "Ввод текста не поддерживается, воспользуйся кнопками.")

@dp.callback_query_handler(lambda c: True)
async def process_callback_language(call):
    try:
        id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        state = chat_states.get(id)
        msg_id = call.message.message_id
        data = call.data

        if data in DCT.banks:
            users_banks[id] = data
            curr_keyboard = await K.get_currency_keyboard(data)
            # Меняем банк
            if state == 'another_bank':
                currency = users_currency.get(id)
                actions_keyboard = await K.get_actions(data)
                await call.message.edit_text(f"Выбранный банк: {data}.\nВыбранная валюта: {currency}.\nВыбери твое следующее действие. 👇",
                                            reply_markup=actions_keyboard)
                chat_states[id] = ''
                return
            # Банк не выбран. После выбора банка, проверяем валюту, если валюта есть, то продолжаем транзакцию.
            if state in functions_calls:
                currency = users_currency.get(id)
                if currency == '':
                    await call.message.edit_text(f"Сначала нужно выбрать валюту!\nВыбери ее списка! 👇",
                                                reply_markup=curr_keyboard)
                    return
                else:
                    actions_keyboard = await K.get_actions(data)
                    await bot.delete_message(id,msg_id)
                    call_functions = functions_calls.get(state)
                    await call_functions(currency)
                    with open(f"{id}_delta.png", "rb") as file:
                        await bot.send_photo(id, file)
                    await bot.send_message(id,
                                        f"Выбранный банк: {data}.\nВыбранная валюта: {currency}.\nВыбери твое следующее действие. 👇",
                                        reply_markup=actions_keyboard)
                    chat_states[id] = ''
                    return

            await call.message.edit_text(f"Ты выбрал {data}, теперь выбери нужную тебе валюту из списка ниже. 👇", reply_markup=curr_keyboard)

        if data in DCT.currency:
            bank = users_banks.get(id)
            actions_keyboard = await K.get_actions(bank)
            curr_keyboard = await K.get_currency_keyboard(bank)
            users_currency[id] = data 
            if state in functions_calls:
                if bank == '':
                    await call.message.edit_text(f"Сначала нужно выбрать валюту!\nВыбери ее списка! 👇",
                                                reply_markup=curr_keyboard)
                    return
                else:
                    await bot.delete_message(id,msg_id)
                    call_functions = functions_calls.get(state)
                    await call_functions(data)
                    with open(f"{id}_delta.png", "rb") as file:
                        await bot.send_photo(id, file)
                    await bot.send_message(id,
                                        f"Выбранный банк: {bank}.\nВыбранная валюта: {data}.\nВыбери твое следующее действие. 👇",
                                        reply_markup=actions_keyboard)
                    chat_states[id] = ''
                    return
            await call.message.edit_text(
                f"Выбранный банк: {bank}.\nВыбранная валюта: {data}.\nВыбери твое следующее действие. 👇",
                reply_markup=actions_keyboard)

        if data in DCT.actions:
            bank = users_banks.get(id)
            currency = users_currency.get(id)
            actions_keyboard = await K.get_actions(bank)
            keyboard_start = await K.get_bank_keyboard()
            curr_keyboard = await K.get_currency_keyboard(bank)
            if data == 'another_bank':
                chat_states[id] = 'another_bank'
                await call.message.edit_text(f"Выбранный банк: {bank}.\nНажми на кнопку, чтобы поменять. 👇",
                                            reply_markup=keyboard_start)
                return
            if data == 'another_currency':
                await call.message.edit_text(f"Выбранная валюта: {currency}.\nНажми на кнопку, чтобы поменять. 👇",
                                            reply_markup=curr_keyboard)
                return
            chat_states[id] = data
            if data == 'choose_date' and bank != 'Альфа Банк':
                return
            elif data == 'choose_date' and bank == 'Альфа Банк':
                return
            if bank == '':
                await call.message.edit_text(f"Сначала нужно выбрать банк!\nВыбери его списка! 👇", reply_markup=keyboard_start)
                return
            if currency == '':
                await call.message.edit_text(f"Сначала нужно выбрать валюту!\nВыбери ее списка! 👇", reply_markup=curr_keyboard)
                return
            await bot.delete_message(id, msg_id)
            call_functions = functions_calls.get(data)
            await call_functions(currency, id)
            with open(f"{id}_delta.png", "rb") as file:
                    await bot.send_photo(id, file)
            await bot.send_message(id,f"Выбранный банк: {bank}.\nВыбранная валюта: {currency}.\nВыбери твое следующее действие. 👇",
                                            reply_markup=actions_keyboard)
            chat_states[id] = ''
            return
    except:
        await bot.send_message(id, "Что-то полшо не так...")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)#, on_startup=on_start, on_shutdown=on_shutdown)