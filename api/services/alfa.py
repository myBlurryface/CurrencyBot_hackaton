import aiohttp

import asyncio
import json


ALPHA_URL = "https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"


async def get_alpha_bank_currency_list():
    async with aiohttp.ClientSession() as session:
        currencies = set()
        url = ALPHA_URL
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for currency in data['rates']:
                    currencies.add(currency["sellIso"])
                currencies = list(currencies)
                print(currencies)
            else:
                print(f"Ошибка запроса: {response.status}")
        return currencies
    
    
async def get_alpha_bank_currency(currency_name: str):
    async with aiohttp.ClientSession() as session:
        currencies = list()
        url = ALPHA_URL
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for currency in data['rates']:
                    if currency["sellIso"] == currency_name and \
                        currency["buyIso"] == "BYN":
                            currencies.append(currency)
                print(currencies)
            else:
                print(f"Ошибка запроса: {response.status}")
        return currencies
    