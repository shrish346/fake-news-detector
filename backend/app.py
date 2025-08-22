from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI()

# To recieve a JSON, input needs to be wrapped in a pydantic model
class TextRequest(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message" : "Welcome to the Fake News Detector API!"}


@app.post("/predict")
def predict_news(request: TextRequest):
    result = predict(request.text)
    return{
        "label": result['label'],
        "score": result['score']
    }



