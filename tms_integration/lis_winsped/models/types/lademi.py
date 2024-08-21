from pydantic import BaseModel, Field, validator
from typing import Optional, Union
from datetime import datetime


class Lademi(BaseModel):
    satzart: str = Field("LADEMI", const=True)
    referenz: Optional[str] = None
    tladenr: Optional[str] = None
    aufnr: Union[str, int, None] = None
    aufposnr: Union[str, int, None] = None
    lademittelart: Optional[str] = None
    palanz: Optional[Union[str, Union[str, int]]] = None
    pal: Optional[str] = None
    laenge: Optional[Union[str, float]] = None
    breite: Optional[Union[str, float]] = None
    hoehe: Optional[Union[str, float]] = None
    eigengew: Optional[Union[str, float]] = None
    nve: Optional[str] = None
    lmart: Union[str, int]
    waufragid: Optional[Union[str, int]] = None
    waufposid: Optional[Union[str, int]] = None
    einhgew: Optional[str] = None
    einhlaenge: Optional[str] = None
    einhbreite: Optional[str] = None
    einhhoehe: Optional[str] = None
    lageplatz: Optional[str] = None

    # @validator(
    #     "belvorhandsdatum", "entvorhandsdatum", "tourdatum", pre=True, each_item=True, allow_reuse=True
    # )
    # def parse_date(cls, value):
    #     if isinstance(value, str):
    #         return datetime.strptime(value, "%Y%m%d")
    #     return value

    # @validator("belvorhandzeit", "entvorhandzeit", "tourzeit", pre=True, each_item=True, allow_reuse=True)
    # def parse_time(cls, value):
    #     if isinstance(value, str):
    #         return datetime.strptime(value, "%H%M").time()
    #     return value
