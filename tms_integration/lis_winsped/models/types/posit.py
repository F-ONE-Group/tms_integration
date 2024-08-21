from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Posit(BaseModel):
    satzart: str = Field("POSIT", const=True)
    referenz: Optional[str] = None
    tladenr: Optional[str] = None
    aufnr: Optional[int] = None
    aufposnr: Optional[int] = None
    refpos: Optional[str] = None
    tatsgew: Optional[float] = None
    fpflgew: Optional[float] = None
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
    ggutgew: Optional[float] = None
    cdmanz: Optional[float] = None
    lmanz: Optional[float] = None
    qmanz: Optional[float] = None
    spanz: Optional[float] = None
    smenge: Optional[float] = None
    imenge: Optional[float] = None
    warenwert: Optional[float] = None
    qualitaet: Optional[int] = None
    wauftragid: Optional[int] = None
    waufposid: Optional[int] = None
    einhgew: Optional[str] = None
    einhvol: Optional[str] = None
    einhlaenge: Optional[str] = None
    einhflaech: Optional[str] = None
    tgew: Optional[float] = None
    hoehe: Optional[float] = None
    breite: Optional[float] = None
    laenge: Optional[float] = None
    taragew: Optional[float] = None
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
    verswert: Optional[float] = None
    shilf1: Optional[str] = None
    shilf2: Optional[str] = None
    shilf3: Optional[str] = None
    lhilf1: Optional[int] = None
    lhilf2: Optional[int] = None
    dtmhilf1: Optional[datetime] = None
    dtmhilf2: Optional[datetime] = None
    curhilf1: Optional[float] = None
    curhilf2: Optional[float] = None
    pspelement: Optional[str] = None
    befkat: Optional[str] = None
    fz: Optional[int] = None
    aendstatus: Optional[str] = None
    solttatsgew: Optional[float] = None
    sollpalanze: Optional[float] = None
    sollvpeanz: Optional[float] = None
    sollmeanz: Optional[float] = None
    sollspanz: Optional[float] = None
    beltxt: Optional[str] = None
    leergut: Optional[int] = None
    umweltgef: Optional[bool] = None
    curhilf3: Optional[float] = None
    curhilf4: Optional[float] = None
    curhilf5: Optional[float] = None
    curhilf6: Optional[float] = None
    curhilf7: Optional[float] = None

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
