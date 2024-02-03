import aiohttp

import asyncio
import json

from api.apps.constants import CurrencyEnum


BELARUSBANK_API = "https://belarusbank.by/api/kurs_cards"


async def get_belarusbank_currency_list() -> list | None:
    async with aiohttp.ClientSession() as session:
        currencies = set()
        url = BELARUSBANK_API
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                currency_list = [currency.name for currency in CurrencyEnum]
                for currency_name in data[0]:
                    currency_short_name = currency_name[:3]
                    if currency_short_name in currency_list:
                        currencies.add(currency_short_name)
                currencies = list(currencies)
            else:
                print(f"Ошибка запроса: {response.status}")
                return None
        return currencies


async def get_belarusbank_currency(currency: str) -> None | list:
    async with aiohttp.ClientSession() as session:
        currencies = []
        url = BELARUSBANK_API
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for currency_name in data[0]:
                    if currency_name.count('_') == 1:
                        currency_short_name = currency_name[:3]
                        if currency_short_name == currency:
                            currencies.append(currency_name)
            else:
                print(f"Ошибка запроса: {response.status}")
                return None
        return currencies
    