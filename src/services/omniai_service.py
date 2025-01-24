import os

from pyzerox import zerox

from src.config.config import OPENAI_API_KEY
from src.models.models import ResponseWithPageNum, TextElementWithPageNum

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


# Define main async entrypoint
async def omniai_service(file_path):
    result = await zerox(
        file_path=file_path,
        model="gpt-4o-mini",
        # maintain_format=True,
        # output_dir=output_dir,
    )
    response = ResponseWithPageNum(
        result=[
            TextElementWithPageNum(text=page.content, page_number=page.page)
            for page in result.pages
        ]
    )
    return response
