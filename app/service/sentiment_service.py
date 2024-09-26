from fastapi import HTTPException
from ..utils.sentiment_utils import extract_reviews

def process_uploaded_files(files: list):
    
    all_review = []
    for file in files:
        if file.filename.endswith('.csv') or file.filename.endswith('.xlsx'):
            filename = file.filename
            print("Processing File", filename)

            reviews = extract_reviews(file)
            
            all_review.extend(reviews)

        else:
            raise HTTPException(status_code=400, detail=f"File is not supported {file.filename}")
    return all_review