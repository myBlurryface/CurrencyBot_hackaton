from fastapi import APIRouter

from api.apps.constants import CurrencyEnum

router = APIRouter(prefix="/rate", tags=["Rate"])

@router.get(
    "/",
    status_code=200,
    summary="Курс валют по дате"
    )
async def currency_by_date(cur_type: str = CurrencyEnum.USD.value):
    ...