from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.services.pdf_service import unstructure_pdf
from src.models.models import Response, tempPathRequest

router = APIRouter()


@router.post(
    "/pdf",
    response_model=Response,
    response_description="List of chunks with page numbers.",
)
async def pdf(request: tempPathRequest):
    """
    This endpoint allows you to extract text from a PDF document.
    It takes a PDF file as input and returns a list of chunks with page numbers.
    """
    try:
        result = unstructure_pdf(request)
        return Response(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
