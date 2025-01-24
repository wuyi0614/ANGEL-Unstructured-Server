from typing import List, Optional, Tuple

from pydantic import BaseModel


class TextElement(BaseModel):
    text: str
    page_number: Optional[int] = None


class Response(BaseModel):
    result: List[TextElement]

    @classmethod
    def from_result(cls, result: List[Tuple[str, Optional[int]]]):
        items = [TextElement(text=item[0], page_number=item[1]) for item in result]
        return cls(result=items)
