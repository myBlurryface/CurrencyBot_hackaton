import aiohttp
from constants import BANK_SHOW
from api.apps.constants import CurrencyEnum
import dicts as DCT


banks_dict = {
    "Альфа Банк": "alfa",
    "Нац Банк": "nb",
    "Беларусь Банк": "belbank"
}

async def get_currency(bank):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8000/api/v1/banks/{banks_dict[bank]}/currencies") as response:
            result = await response.json()

    DCT.currency = [item.get("name") for item in result]
    return DCT.currency

async def get_banks_list():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000/api/v1/banks") as response:
            result = await response.json()
    DCT.banks = [BANK_SHOW.get(r.get("name")) for r in result]
    return DCT.banks
