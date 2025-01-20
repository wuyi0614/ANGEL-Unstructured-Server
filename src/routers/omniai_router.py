import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from pyzerox.core.types import ZeroxOutput
from src.services.omniai_service import omniai_service

router = APIRouter()


@router.post(
    "/omniai",
    response_model=ZeroxOutput,
    response_description="List of chunks with page numbers.",
)
async def omniai(file: UploadFile = File(...)):
    """
    This endpoint allows you to extract text from a document by OmniAI.
    """
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

        try:
            result = await omniai_service(tmp_path)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
