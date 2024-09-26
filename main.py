import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import sentiment_analysis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(sentiment_analysis.router, prefix="/analyse", tags=['sentiment analysis'])


@app.get('/')
def home():
    return {"Message": "welcome to the Home Page"}

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)