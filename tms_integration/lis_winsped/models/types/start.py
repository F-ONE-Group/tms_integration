from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Start(BaseModel):
    satzart: str = Field("START", const=True)
    referenz: str
    erstellt: Optional[datetime] = None
    eigiln: Optional[str] = None
    eigkreid: Optional[str] = None
    eigname1: Optional[str] = None
    expiln: Optional[str] = None
    expempid: Optional[str] = None
    expname1: Optional[str] = None
    impart: Optional[int] = None
    maplfdnr: Optional[int] = None
    status: Optional[str] = None
    versinfo: Optional[str] = None
    skalierungtext1: Optional[str] = None
    skalierungtext2: Optional[str] = None
    skalierungtext3: Optional[str] = None
    skalierungzahl1: Optional[int] = None
    skalierungzahl2: Optional[int] = None
    skalierungdatum1: Optional[datetime] = None
    skalierungdatum2: Optional[datetime] = None

    @validator(
        "erstellt", "skalierungdatum1", "skalierungdatum2", pre=True, each_item=True
    )
    def parse_datetime(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y%m%d%H%M%S")
        return value

    @validator("status")
    def validate_status(cls, value):
        if value not in {"D", "L", "Z", "E", "F"}:
            raise ValueError("Invalid status value")
        return value
