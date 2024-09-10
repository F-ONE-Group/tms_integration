from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Geb(BaseModel):
    satzart: str = Field("GEB", const=True)
    referenz: str
    tladenr: str
    aufnr: int
    kunart: int
    menge: Optional[str] = None
    betrag: Optional[str] = None
    waehr: Optional[str] = None
    ucprz: Optional[str] = None
    abreart: Optional[str] = None
    infotext: Optional[str] = None