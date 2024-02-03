import api_calls as APIS
from aiogram import types

async def get_bank_keyboard():
    keyboard_start = types.InlineKeyboardMarkup(row_width=2)
    banks_list = APIS.get_banks_list()
    for i in range(0, banks_list-2):
        keyboard_start.add(types.InlineKeyboardButton(text=banks_list[i], callback_data=banks_list[i+1]),
                          types.InlineKeyboardButton(text=banks_list[i], callback_data=banks_list[i+1]))
    return keyboard_start

async def get_currency_keyboard():
    currency_list = APIS.get_currency()
    curr_keyboard = types.InlineKeyboardMarkup(row_width=2)
    for i in range(0, len(currency_list) - 2):
        curr_keyboard.add(types.InlineKeyboardButton(text=currency_list[i], callback_data=currency_list[i+1]),
                          types.InlineKeyboardButton(text=currency_list[i], callback_data=currency_list[i+1]))
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