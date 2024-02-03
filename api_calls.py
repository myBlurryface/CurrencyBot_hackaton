import aiohttp
from constants import BANK_SHOW
from api.apps.constants import CurrencyEnum
from api.services.nb import get_national_bank_currency_delta
import dicts as DCT

from datetime import datetime

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

async def get_file(cur_code, user_id):
    result = await get_national_bank_currency_delta(cur_code, user_id)


async def get_currency_by_date(*args, **kwargs):
    bank_name = kwargs.get("bank")
    bank = banks_dict.get(bank_name)
    code = kwargs.get("code")
    date = datetime.now()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:8000/api/v1/rate?bank={bank}&currency_code={code}&date={date}") as response:
            result = await response.json()
    rate = result.get("rate")
    text = f"Банк - {bank_name}\nВалюта - {code}\nДата - {date.date()}\nКурс - {rate}"
    return text

functions_calls = {
'statistics': get_file,
}