from enum import Enum


class BankEnum(Enum):
    ALFA: str = "alfa"
    NB: str = "nb"
    BElARUSBANK: str = "belbank"

class CurrencyEnum(Enum):
    USD: str = "USD"
    EUR: str = "EUR"
    GBP: str = "GBP"
    JPY: str = "JPY"