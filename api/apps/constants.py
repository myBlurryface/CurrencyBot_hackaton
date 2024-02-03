from enum import Enum


class BankEnum(Enum):
    ALFA: str = "alfa"
    NB: str = "nb"
    BElARUSBANK: str = "belbank"

class CurrencyEnum(Enum):
    USD: str = "usd"
    EUR: str = "eur"
    GBP: str = "gbp"
    JPY: str = "jpy"