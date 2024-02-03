from fastapi import APIRouter

from api.apps.constants import CurrencyEnum, BankEnum
from api.apps.banks.schemes import CurrencyScheme, BankScheme
from api.apps.currencies.scheme import CurrencyInfoScheme
from api.services.nb import get_national_bank_currency_by_date

from datetime import datetime

router = APIRouter(prefix="/rate", tags=["Rate"])


bank_dict = {
    BankEnum.NB: get_national_bank_currency_by_date
}

@router.get(
    "/",
    status_code=200,
    summary="Курс валют по дате",
    response_model=CurrencyInfoScheme
    )
async def currency_by_date(
    currency_code: CurrencyEnum,
    bank: BankEnum,
    date: datetime = datetime.today()
    ):
    implement = bank_dict.get(bank)
    result = await implement(currency_code.value.upper(), date.date())
    return CurrencyInfoScheme(
        bank=bank,
        date=date.date(),
        code=currency_code,
        rate=result.get("Cur_OfficialRate")
    )

@router.get(
    "/rates",
    status_code=200,
    summary="Курс валют в промежуток времени"
    )
async def currency__interval(
    currency_code: CurrencyEnum,
    bank: BankEnum,
    start: datetime,
    end: datetime
    ):
    ...

@router.get(
    "/statistics",
    status_code=200,
    summary="Статистика валюты",
    )
async def get_stattistic(
    currency_code: CurrencyEnum,
    bank: BankEnum,
    start: datetime,
    end: datetime,
    ):
    ...