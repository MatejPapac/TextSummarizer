from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

text: str = 'What is Text Summarization'

app = FastAPI()

@app.get("/", tags=['authentication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return {"message": "Training Completed"}
    except Exception as e:
        return {"message": str(e)}

@app.post("/predict")
async def predict(text: str):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
