from pydantic import BaseModel, Field
from typing import Optional


class DmsSw(BaseModel):
    satzart: str = Field("DMSSW", const=True)
    referenz: str
    dmsdoknr: int
    dmsswnr: int
    schluessel: str
    wert: str
