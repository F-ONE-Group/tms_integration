from pydantic import BaseModel, Field
from typing import Optional


class DmsRef(BaseModel):
    satzart: str = Field("DMSREF", const=True)
    referenz: str
    dmsdoknr: int
    dmsrefnr: int
    aufnr: int
    kundennr: Optional[str]
    liefnr: Optional[str]
    refnr: Optional[str]
    kommnr: Optional[str]
