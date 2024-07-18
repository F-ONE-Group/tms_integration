from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Lademi(BaseModel):
    satzart: str = Field("LADEMI", const=True)
    referenz: str
    tladenr: str
    aufnr: int
    aufposnr: int
    lademittelart: str
    anz: Optional[int] = None
    lademittelid: Optional[str] = None
    kostenst: Optional[str] = None
    eigengewicht: Optional[float] = None
    kumulierbarkeit: Optional[str] = None
    pfand: Optional[float] = None
    behaelter: Optional[str] = None
    uebergabeart: Optional[str] = None
    status: Optional[str] = None
    belvorhandsdatum: Optional[datetime] = None
    belvorhandzeit: Optional[str] = None
    belabgeschlossen: Optional[str] = None
    entvorhandsdatum: Optional[datetime] = None
    entvorhandzeit: Optional[str] = None
    entabgeschlossen: Optional[str] = None
    tourdatum: Optional[datetime] = None
    tourzeit: Optional[str] = None

    @validator(
        "belvorhandsdatum", "entvorhandsdatum", "tourdatum", pre=True, each_item=True
    )
    def parse_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y%m%d")
        return value

    @validator("belvorhandzeit", "entvorhandzeit", "tourzeit", pre=True, each_item=True)
    def parse_time(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%H%M").time()
        return value
