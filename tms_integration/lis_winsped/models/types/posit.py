from pydantic import BaseModel, Field, validator
from typing import Optional, Union
from datetime import datetime


class Posit(BaseModel):
    satzart: str = Field("POSIT", const=True)
    referenz: Optional[str] = None
    tladenr: Optional[str] = None
    aufnr: Optional[int] = None
    aufposnr: Optional[int] = None
    refpos: Optional[str] = None
    tatsgew: Optional[Union[str, float]] = None
    fpflgew: Optional[Union[str, float]] = None
    ean: Optional[str] = None
    artnre: Optional[str] = None
    artnrl: Optional[str] = None
    artikel: Optional[str] = None
    zeichen: Optional[str] = None
    inhalt: Optional[str] = None
    tarifid: Optional[str] = None
    ggutklasse: Optional[str] = None
    ggutunr: Optional[str] = None
    ggutziffer: Optional[str] = None
    ggutgew: Optional[Union[str, float]] = None
    cdmanz: Optional[Union[str, float]] = None
    lmanz: Optional[Union[str, float]] = None
    qmanz: Optional[Union[str, float]] = None
    spanz: Optional[Union[str, float]] = None
    smenge: Optional[Union[str, float]] = None
    imenge: Optional[Union[str, float]] = None
    warenwert: Optional[Union[str, float]] = None
    qualitaet: Optional[int] = None
    wauftragid: Optional[int] = None
    waufposid: Optional[int] = None
    einhgew: Optional[str] = None
    einhvol: Optional[str] = None
    einhlaenge: Optional[str] = None
    einhflaech: Optional[str] = None
    tgew: Optional[Union[str, float]] = None
    hoehe: Optional[Union[str, float]] = None
    breite: Optional[Union[str, float]] = None
    laenge: Optional[Union[str, float]] = None
    taragew: Optional[Union[str, float]] = None
    stapelhoe: Optional[float] = None
    kammer: Optional[str] = None
    inhalt2: Optional[str] = None
    hbuchkto: Optional[str] = None
    kostena: Optional[str] = None
    innenaufnr: Optional[str] = None
    vertrieb: Optional[int] = None
    matart: Optional[str] = None
    matgrp: Optional[str] = None
    sparte: Optional[str] = None
    gklasse: Optional[str] = None
    ggruppe: Optional[str] = None
    verswert: Optional[Union[str, float]] = None
    shilf1: Optional[str] = None
    shilf2: Optional[str] = None
    shilf3: Optional[str] = None
    lhilf1: Optional[int] = None
    lhilf2: Optional[int] = None
    dtmhilf1: Optional[datetime] = None
    dtmhilf2: Optional[datetime] = None
    curhilf1: Optional[Union[str, float]] = None
    curhilf2: Optional[Union[str, float]] = None
    pspelement: Optional[str] = None
    befkat: Optional[str] = None
    fz: Optional[int] = None
    aendstatus: Optional[str] = None
    solttatsgew: Optional[Union[str, float]] = None
    sollpalanze: Optional[Union[str, float]] = None
    sollvpeanz: Optional[Union[str, float]] = None
    sollmeanz: Optional[Union[str, float]] = None
    sollspanz: Optional[Union[str, float]] = None
    beltxt: Optional[str] = None
    leergut: Optional[int] = None
    umweltgef: Optional[bool] = None
    curhilf3: Optional[Union[str, float]] = None
    curhilf4: Optional[Union[str, float]] = None
    curhilf5: Optional[Union[str, float]] = None
    curhilf6: Optional[Union[str, float]] = None
    curhilf7: Optional[Union[str, float]] = None

    @validator("dtmhilf1", "dtmhilf2", pre=True, each_item=True)
    def parse_datetime(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y%m%d")
        return value

    @validator("aendstatus")
    def validate_aendstatus(cls, value):
        if value and value not in {"N", "A", "L"}:
            raise ValueError("Invalid Aendstatus value")
        return value

    @validator("umweltgef")
    def validate_boolean(cls, value):
        if value not in {None, True, False}:
            raise ValueError("Invalid boolean value")
        return value
