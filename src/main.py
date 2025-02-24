from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# from fastapi.staticfiles import StaticFiles

from src.config.config import FASTAPI_AUTH, FASTAPI_BEARER_TOKEN
from src.routers import health_router, pdf_router, omniai_router, docx_router, ppt_router

load_dotenv()

bearer_scheme = HTTPBearer()


def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or credentials.credentials != FASTAPI_BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return credentials


app = FastAPI(
    title="ANGEL-NTU Unstructured Server",
    version="1.0",
    description="ANGEL-NTU Unstructured API Server",
    dependencies=[Depends(validate_token)] if FASTAPI_AUTH else None,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router.router)
app.include_router(pdf_router.router)
app.include_router(omniai_router.router)
app.include_router(docx_router.router)
app.include_router(ppt_router.router)
