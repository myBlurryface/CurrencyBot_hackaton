import aiohttp
from constants import BANK_SHOW
from api.apps.constants import CurrencyEnum


banks_dict = {
    "Альфа Банк": "alfa",
    "Нац Банк": "nb",
    "Беларусь Банк": "belbank"
}

async def get_currency():
    currency_list = []
    
    return currency_list

async def get_banks_list():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000/api/v1/banks") as response:
            result = await response.json()
    return [(BANK_SHOW.get(r.get("name")), banks_dict.get(BANK_SHOW.get(r.get("name")))) for r in result]