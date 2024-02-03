from fastapi import APIRouter

from api.apps.constants import CurrencyEnum, BankEnum
from api.apps.banks.schemes import CurrencyScheme, BankScheme

from datetime import datetime

router = APIRouter(prefix="/rate", tags=["Rate"])

@router.get(
    "/",
    status_code=200,
    summary="Курс валют по дате"
    )
async def currency_by_date(
    currency_code: CurrencyEnum,
    bank: BankEnum,
    date: datetime = datetime.today()
    ):
    ...

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