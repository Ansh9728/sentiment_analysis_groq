import pandas as pd
from io import StringIO, BytesIO
from groq import Groq
import os


def extract_reviews(file):

    if file.filename.endswith('.csv'):
        
        file_content = file.file.read().decode('utf-8')
        df = pd.read_csv(StringIO(file_content))

    elif file.filename.endswith('.xlsx'):
        file_content = file.file.read()
        df = pd.read_excel(BytesIO(file_content), engine='openpyxl')

    if 'Review' not in df.columns:
        raise ValueError("The file does not contain a 'Review' column")

    return df['Review'].tolist()


def get_sentiment(review):

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a data analyst API capable of sentiment analysis that responds in JSON.  Only Include The JSON schema should include\n{\n  \"sentiment_analysis\": {\n    \"sentiment\":  {\n       \"positive\": score,\n       \"negative\": score,\n       \"neutral\": score\n     },\n    \"confidence_score\": \"number (0-1)\"\n  }\n}"
            },
            {
                "role": "user",
                "content": str(review)
            }
        ],
        temperature=0,
        max_tokens=512,
        top_p=1,
        stream=False,
        stop=None,
        response_format={"type": "json_object"}
    )
     
    res = completion.choices[0].message.content
    return res
    

def perform_sentiment_analysis(reviews: list):
    result = []
    for review in reviews:
        sentiment = get_sentiment(review=review)
        sentiment_review = {
            "review": review,
            "sentiment": sentiment
        }
        result.append(sentiment_review)

    df = pd.DataFrame(result)
    df.to_csv(os.path.join(os.getcwd(), "Data_Folder/output.csv"))
    return result
