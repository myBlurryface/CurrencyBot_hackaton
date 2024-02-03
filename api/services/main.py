import aiohttp

import asyncio
import json


USD_LINK = "https://api.nbrb.by/exrates/rates/USD?parammode=2"
EUR_LINK = "https://api.nbrb.by/exrates/rates/EUR?parammode=2"
GBP_LINK = "https://api.nbrb.by/exrates/rates/GBP?parammode=2"
JPY_LINK = "https://api.nbrb.by/exrates/rates/JPY?parammode=2"


async def get_national_bank_currencies_list():
    async with aiohttp.ClientSession() as session:
        currencies = []
        url = "https://api.nbrb.by/exrates/currencies"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                for currency in data:
                    currencies.append(currency["Cur_Abbreviation"])
            else:
                print(f"Ошибка запроса: {response.status}")
        return currencies


async def get_national_bank_currency():
    async with aiohttp.ClientSession() as session:
        url = "https://api.nbrb.by/exrates/rates/USD?parammode=2"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
            else:
                print(f"Ошибка запроса: {response.status}")
                
                
async def get_national_bank():
    async with aiohttp.ClientSession() as session:
        url = "https://api.nbrb.by/exrates/rates/USD?parammode=2"
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
            else:
                print(f"Ошибка запроса: {response.status}")
    
    
if __name__ == "__main__":
    asyncio.run(get_national_bank_currencies())
    # asyncio.run(get_national_bank())
