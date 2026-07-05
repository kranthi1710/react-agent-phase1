from typing import ClassVar
from pydantic import BaseModel
class Settings(BaseModel):
    MODEL: ClassVar[str] = 'llama3.2'
    TEMPERATURE: ClassVar[float] = 0.2

settings = Settings()
