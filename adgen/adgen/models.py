from pydantic import BaseModel
from typing import Literal


class PostRequest(BaseModel):
    title: str
    description: str
    tone: Literal["friendly", "expert", "funny"] = "friendly"
