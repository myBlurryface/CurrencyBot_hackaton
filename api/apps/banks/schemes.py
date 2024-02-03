from pydantic import BaseModel

from  api.apps.constants import BankEnum


class BankScheme(BaseModel):
    name: BankEnum