from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Text(BaseModel):
    satzart: str = Field("TEXT", const=True)
    referenz: str
    tladenr: str
    aufnr: int
    txtartnr: int
    txtstr1: str
    gtext: Optional[bool] = None
    txtstr2: Optional[str] = None
    txtstr3: Optional[str] = None
    txtstr4: Optional[str] = None
    txtstr5: Optional[str] = None
    txtdatum: Optional[datetime] = None

    @validator("txtdatum", pre=True)
    def parse_date(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y%m%d")
        return value

    @validator("gtext")
    def validate_boolean(cls, value):
        if value not in {None, True, False}:
            raise ValueError("Invalid boolean value")
        if value == False:
            return "N"  # Nein
        elif value == True:
            return "J"  # Ja
        return value
