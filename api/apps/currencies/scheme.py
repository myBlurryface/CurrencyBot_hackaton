from pydantic import BaseModel

from datetime import date

class CurrencyInfoScheme(BaseModel):
    bank: str
    date: date
    code: str
    rate: float