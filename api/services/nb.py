import aiohttp
import matplotlib.pyplot as plt

import asyncio
import json
import calendar
from datetime import date


USD_LINK = "https://api.nbrb.by/exrates/rates/USD?parammode=2"
EUR_LINK = "https://api.nbrb.by/exrates/rates/EUR?parammode=2"
GBP_LINK = "https://api.nbrb.by/exrates/rates/GBP?parammode=2"
JPY_LINK = "https://api.nbrb.by/exrates/rates/JPY?parammode=2"

CURRENCIES = {
    "USD": USD_LINK,
    "EUR": EUR_LINK,
    "GBP": GBP_LINK,
    "JPY": JPY_LINK,
}


async def get_national_bank_currencies_list() -> list | None:
    """
    Getting information about available rates in Natianal Bank of 
    Republic Of Belarus.
    :return:
    """
    async with aiohttp.ClientSession() as session:
        currencies = []
        url = "https://api.nbrb.by/exrates/currencies"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for currency in data:
                    currencies.append(currency["Cur_Abbreviation"])
                return currencies
            else:
                print(f"Ошибка запроса: {response.status}")
    return None


async def get_national_bank_currency(currency: str) -> dict | None:
    async with aiohttp.ClientSession() as session:
        try:
            url = CURRENCIES[currency]
        except Exception:
            return None
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                print()
    return None


async def get_national_bank_currency_by_date(currency_name: str, date) -> dict | None:
    async with aiohttp.ClientSession() as session:
        url = f"https://api.nbrb.by/exrates/rates?ondate={date}&periodicity=0"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for currency in data:
                    if currency["Cur_Abbreviation"] == currency_name:
                        print(currency)
                        return currency
            else:
                print(f"Ошибка запроса: {response.status}")
    return None


async def get_national_bank_currency_delta(currency_name: str) -> dict | None:
    today = date.today()
    year = today.year
    month = today.month
    if month == 1:
        month = 12
        year -= 1
    else:
        month -= 1
    dates = calendar.Calendar().itermonthdates(year, month)
    courses = dict()
    for months_date in dates:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.nbrb.by/exrates/rates?ondate={months_date}&periodicity=0"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    for currency in data:
                        if currency["Cur_Abbreviation"] == currency_name:
                            courses[f"{months_date}"] = currency["Cur_OfficialRate"]
                else:
                    return None
                    print(f"Ошибка запроса: {response.status}")
    build_graph_by_day(courses)
    return courses


def build_graph_by_day(currency_cource: dict):
    dates = list(currency_cource.keys())
    rates = list(currency_cource.values())
    
    plt.plot(dates, rates)
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.title("Изменение курса валюты")
    plt.savefig("nb_delta.png")
