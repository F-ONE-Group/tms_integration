from typing import List
from datetime import datetime, time
from pydantic import BaseModel

from .types import *


class LisIn(BaseModel):
    start: Start
    ladeli: List[Ladeli]
    auftr: List[Auftrag]
    posit: List[Posit]
    lademi: List[Lademi] = []
    ggut: List[Ggut]
    adr: List[Adr]
    text: List[Text]
    ende: Ende

    def generate_txt(self) -> str:
        lines = []

        def model_to_line(model):
            fields = []
            for field_key in model.__fields__.keys():
                field_value = model.dict().get(field_key)
                if field_value:
                    if isinstance(field_value, datetime):
                        fields.append(field_value.strftime("%Y%m%d"))
                    elif isinstance(field_value, time):
                        fields.append(field_value.strftime("%H%M"))
                    else:
                        fields.append(str(field_value))
                else:
                    fields.append("")
            return "|".join(fields)

        lines.append(model_to_line(self.start))
        for ladeli in self.ladeli:
            lines.append(model_to_line(ladeli))
        for auftr in self.auftr:
            lines.append(model_to_line(auftr))
        for posit in self.posit:
            lines.append(model_to_line(posit))
        for lademi in self.lademi:
            lines.append(model_to_line(lademi))
        for ggut in self.ggut:
            lines.append(model_to_line(ggut))
        for adr in self.adr:
            lines.append(model_to_line(adr))
        for text in self.text:
            lines.append(model_to_line(text))
        lines.append(model_to_line(self.ende))

        return "\n".join(lines)
