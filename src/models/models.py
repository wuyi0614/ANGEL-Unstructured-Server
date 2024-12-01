from typing import List, Tuple

from pydantic import BaseModel


class TextElement(BaseModel):
    text: str
    page_number: int


class Response(BaseModel):
    result: List[TextElement]

    @classmethod
    def from_result(cls, result: List[Tuple[str, int]]):
        items = [TextElement(text=item[0], page_number=item[1]) for item in result]
        return cls(result=items)
