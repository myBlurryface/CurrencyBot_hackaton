from fastapi import APIRouter
from fastapi.responses import JSONResponse

from typing import List

from api.apps.constants import BankEnum
from api.apps.banks.schemes import BankScheme

router = APIRouter(prefix="/banks", tags=["Bank"])


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
        summary="Валюты по банку"
        )
async def detail_bank(bank_name: str):
    bank = [bank.value for bank in BankEnum if bank.value == bank_name]
    if not bank:
        return JSONResponse(content={"Status": "Error", "Msg": "Bank doesn't exists"}, status_code=404)
    return # Currencies