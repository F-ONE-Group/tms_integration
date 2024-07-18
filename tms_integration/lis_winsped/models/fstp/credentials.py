from pydantic import BaseModel
import pysftp


class Credentials(BaseModel):
    username: str
    password: str
    host: str
    port: int = 22
