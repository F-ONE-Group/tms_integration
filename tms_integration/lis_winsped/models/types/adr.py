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
    ortt: Optional[str] = None
    pfach: Optional[str] = None
    pfachplz: Optional[str] = None
    tel: Optional[str] = None
    fax: Optional[str] = None
    mc: Optional[str] = None
    partner: Optional[str] = None
    kontotab: Optional[int] = None
    kstelle: Optional[int] = None
    bundesland: Optional[str] = None
    wadrid: Optional[str] = None
    wupddatum: Optional[str] = None
    ktraeger: Optional[int] = None
    ustnr: Optional[str] = None
    uscheidnr: Optional[int] = None
    zollnr: Optional[str] = None
    gruppe: Optional[str] = None
    abholff: Optional[int] = None
    emailadr: Optional[str] = None
    statistik1: Optional[str] = None
    statistik2: Optional[str] = None
    statistik3: Optional[str] = None
    statistik4: Optional[str] = None
    statistik5: Optional[str] = None
    name3: Optional[str] = None
    orgkundennr: Optional[int] = None
    kuntemp: Optional[str] = None
    ortgeox: Optional[int] = None
    ortgeoy: Optional[int] = None
    ortgeoxk: Optional[int] = None
    ortgeoyk: Optional[int] = None
    ortelfdnr: Optional[int] = None
    kundennra: Optional[str] = None
    ktodeb: Optional[int] = None
    ktokre: Optional[int] = None
    telauto: Optional[str] = None
    uc: Optional[str] = None
    ustid: Optional[str] = None
    steuernr: Optional[str] = None
    zahlbed: Optional[str] = None
    frankatur: Optional[str] = None
    verkart: Optional[str] = None
    sprache: Optional[int] = None
    reperiode: Optional[str] = None
    rewaehr: Optional[str] = None
    gsperiode: Optional[str] = None
    gswaehr: Optional[str] = None
    konzernnr: Optional[int] = None
    abwrekunnr: Optional[int] = None
    abwgskunnr: Optional[int] = None
    homepage: Optional[str] = None
    info: Optional[str] = None
    cmrzubis: Optional[str] = None
    cmrzubetr: Optional[float] = None
    cmrzuwaeh: Optional[str] = None
    kvobis: Optional[str] = None
    kvobetrag: Optional[float] = None
    kvowaehr: Optional[str] = None
    cmrdatum: Optional[str] = None
    dmrbetrag: Optional[float] = None
    cmrwaehr: Optional[str] = None
    extadrnr: Optional[str] = None
    ppbetragre: Optional[float] = None
    ppbetraggs: Optional[float] = None
    kabodat: Optional[str] = None
    adrarteig: Optional[str] = None
    adrreflfd: Optional[int] = None
    ktodeba: Optional[str] = None
    ktokrea: Optional[str] = None
    borderonr: Optional[str] = None
    milogdat: Optional[str] = None
    uiccountry: Optional[int] = None
    uicnr: Optional[int] = None
    uirrnr: Optional[int] = None
    opsaldo: Optional[float] = None
    kredlimit: Optional[float] = None
    guthsaldo: Optional[float] = None
    guthlimit: Optional[float] = None
    limitkz: Optional[int] = None
    sperre: Optional[bool] = None
    sperrdatum: Optional[str] = None
    sperrgrund: Optional[str] = None
    bonitaet: Optional[str] = None
    bonitaetsgrenze: Optional[str] = None
    locode: Optional[str] = None


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
