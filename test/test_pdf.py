# A testfile for PDF router service

from pathlib import Path
from src.routers.pdf_router import unstructure_pdf

# global settings
ROOT = Path('test')
TMP_FILE = ROOT / 'testfile.pdf'


def test_unstructure_pdf():
    result = unstructure_pdf(str(TMP_FILE))
    assert len(result) > 0, 'the function is blocked: unstructure_pdf!'


if __name__ == '__main__':
    # run the following tests before launching, and it will get your HF models ready
    test_unstructure_pdf()
