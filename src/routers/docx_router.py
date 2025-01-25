import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from src.models.models import ResponseWithoutPageNum
from src.services.docx_service import unstructure_docx

router = APIRouter()


@router.post(
    "/docx",
    response_model=ResponseWithoutPageNum,
    response_description="List of chunks.",
)
async def docx(file: UploadFile = File(...)):
    """
    This endpoint allows you to extract text from a PDF document.
    It takes a PDF file as input and returns a list of chunks with page numbers.
    """
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

        try:
            result = unstructure_docx(tmp_path)
            return ResponseWithoutPageNum.from_result(result)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
