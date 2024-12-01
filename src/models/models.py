from typing import List, Optional

from pydantic import BaseModel


class TextElement(BaseModel):
    text: str
    page_number: int


class Response(BaseModel):
    text_list: List[TextElement]


class tempPathRequest(BaseModel):
    tmp_path: str
