import aiohttp

import asyncio
import json

from api.apps.constants import CurrencyEnum


BELARUSBANK_API = "https://belarusbank.by/api/kurs_cards"


async def get_belarusbank_currency_list():
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
                print(currencies)
            else:
                print(f"Ошибка запроса: {response.status}")
        return currencies
    
    
if __name__ == "__main__":
    asyncio.run(get_belarusbank_currency_list())
    