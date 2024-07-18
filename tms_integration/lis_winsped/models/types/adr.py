from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime


class Adr(BaseModel):
    satzart: str = Field("ADR", const=True)
    referenz: str
    tladenr: str
    aufnr: int
    kunart: int
    kundennr: int
    iln: Optional[str] = None
    name1: Optional[str] = None
    name2: Optional[str] = None
    strasse: Optional[str] = None
    lkz: Optional[str] = None
    plz: Optional[str] = None
    ort: Optional[str] = None
    tel: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    adrc: Optional[str] = None
    atsnr: Optional[str] = None
    mobile: Optional[str] = None
    bildnr: Optional[str] = None
    adrkz: Optional[str] = None
    adzeitzonen: Optional[str] = None
    adtag: Optional[str] = None
    adrlieferbedingungen: Optional[str] = None
    bankverbindung: Optional[str] = None
    status: Optional[str] = None
    versinfo: Optional[str] = None

    @validator("status")
    def validate_status(cls, value):
        if value and value not in {"A", "I"}:
            raise ValueError("Invalid status value")
        return value

    @validator("email")
    def validate_email(cls, value):
        if value and "@" not in value:
            raise ValueError("Invalid email address")
        return value

    @validator("plz")
    def validate_plz(cls, value):
        if value and not value.isdigit():
            raise ValueError("Postal code must be numeric")
        return value
