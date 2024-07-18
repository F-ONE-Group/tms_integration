from pydantic import BaseModel, Field


class Ende(BaseModel):
    satzart: str = Field("ENDE", const=True)
