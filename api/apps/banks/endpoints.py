from fastapi import APIRouter
from fastapi.responses import JSONResponse

from typing import List

from api.apps.constants import BankEnum, CurrencyEnum
from api.apps.banks.schemes import BankScheme, CurrencyScheme
from api.services.nb import get_national_bank_currencies_list
from api.services.alfa import get_alpha_bank_currency_list
from api.services.belarusbank import get_belarusbank_currency_list

router = APIRouter(prefix="/banks", tags=["Bank"])


banks_methods = {
    BankEnum.NB.name: get_national_bank_currencies_list,
    BankEnum.ALFA.name: get_alpha_bank_currency_list,
    BankEnum.BElARUSBANK.name: get_belarusbank_currency_list
}


@router.get(
        "/",
        status_code=200,
        response_model=List[BankScheme],
        summary="Список банков"
        )
async def get_banks():
    """
    Отдает список банков
    """
    return [BankScheme(name=bank.value) for bank in BankEnum]

@router.get(
        "/{bank_name}/currencies", 
        status_code=200,
        response_model=List[CurrencyScheme],
        summary="Валюты по банку"
        )
async def detail_bank(bank_name: BankEnum):
    bank = [bank.value for bank in BankEnum if bank.value == bank_name.value]
    if not bank:
        return JSONResponse(content={"Status": "Error", "Msg": "Bank doesn't exists"}, status_code=404)
    implemet = banks_methods.get(bank_name.name)
    currencies_list: List[str] = await implemet()
    currensie_set = set(currencies_list).intersection(set([bank.name for bank in CurrencyEnum]))
    print(currencies_list, currensie_set)
    return [CurrencyScheme(name=currency) for currency in currensie_set]