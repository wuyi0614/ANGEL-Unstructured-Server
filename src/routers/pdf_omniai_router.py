import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from pyzerox.core.types import ZeroxOutput
from src.services.pdf_omniai_service import omniai

router = APIRouter()


@router.post(
    "/pdf-omniai",
    response_model=ZeroxOutput,
    response_description="List of chunks with page numbers.",
)
async def pdf(file: UploadFile = File(...)):
    """
    This endpoint allows you to extract text from a PDF document.
    It takes a PDF file as input and returns a list of chunks with page numbers.
    """
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

        try:
            result = await omniai(tmp_path)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
