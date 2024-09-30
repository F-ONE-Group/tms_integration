from pydantic import BaseModel, Field
from typing import Optional


class DmsDok(BaseModel):
    satzart: str = Field("DMSDOK“", const=True)
    referenz: str
    dmsdoknr: int
    archiv: str
    ordner: str
    doktyp: str
    quellpfad: str
    aendstatus: Optional[str]
