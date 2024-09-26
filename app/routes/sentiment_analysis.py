from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import UploadFile, File
# from service.sentiment_service import process_uploaded_files
from ..service.sentiment_service import process_uploaded_files
from ..utils.sentiment_utils import perform_sentiment_analysis


router = APIRouter()

@router.post('/')
def upload(files: list[UploadFile] = File(...)):
    try:
        reviews = process_uploaded_files(files)
        result = perform_sentiment_analysis(reviews)
        return result

    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))