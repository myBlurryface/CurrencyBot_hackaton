from pydantic import BaseModel

from  api.apps.constants import BankEnum, CurrencyEnum


class BankScheme(BaseModel):
    name: BankEnum

class CurrencyScheme(BaseModel):
    name: CurrencyEnum