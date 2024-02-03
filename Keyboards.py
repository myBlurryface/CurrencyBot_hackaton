import api_calls as APIS
from aiogram import types

async def get_bank_keyboard():
    keyboard_start = types.InlineKeyboardMarkup(row_width=1)
    banks_list = await APIS.get_banks_list()
    for item in banks_list:
        keyboard_start.add(types.InlineKeyboardButton(text=item, callback_data=item))
    return keyboard_start

async def get_currency_keyboard(bank):
    currency_list = await APIS.get_currency(bank)
    curr_keyboard = types.InlineKeyboardMarkup(row_width=2)
    for item in currency_list:
        curr_keyboard.add(types.InlineKeyboardButton(text=item, callback_data=item))
    return curr_keyboard

async def get_actions(alfa_check):
    if alfa_check == 'Альфа Банк':
        actions_keyboard = types.InlineKeyboardMarkup(row_width=2).add(
                      types.InlineKeyboardButton('Курс на текущий день', callback_data=f'same_day'),
                           types.InlineKeyboardButton('Собрать статистику', callback_data='statistics'),
                           ).add(types.InlineKeyboardButton('Выбрать другой банк', callback_data='another_bank'),
                           types.InlineKeyboardButton('Другая валюта', callback_data='another_currency'),
                           )
    else:
        actions_keyboard = types.InlineKeyboardMarkup(row_width=2).add(
                      types.InlineKeyboardButton('Курс на текущий день', callback_data=f'same_day'),
                           types.InlineKeyboardButton('Курс на выбранный день', callback_data='choose_date'),
                           types.InlineKeyboardButton('Собрать статистику', callback_data='statistics'),
                           ).add(types.InlineKeyboardButton('Выбрать другой банк', callback_data='another_bank'),
                           types.InlineKeyboardButton('Другая валюта', callback_data='another_currency'),
                           )
    return actions_keyboard