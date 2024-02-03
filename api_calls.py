import aiohttp
from constants import BANK_SHOW
from api.apps.constants import CurrencyEnum
from api.services.nb import get_national_bank_currency_delta
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

async def get_file(cur_code):
    result = await get_national_bank_currency_delta(cur_code)



functions_calls = {
'statistics': get_file,
}