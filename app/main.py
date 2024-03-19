from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pymongo.errors import DuplicateKeyError
from app.db import metrics
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Metrics Microservice"

@app.get("/metrics/sign-up")
async def get_sign_up_metrics():
    try:
        metrics_array = metrics.find_one({"type": "sign_up"}, {"_id": 0})

        if not metrics_array:
            raise HTTPException(status_code=404, detail="Metric Not Found")
        return metrics_array
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Metric Not Found: {str(e)}")

@app.get("/metrics/country")
async def get_country_metrics():
    try:
        metrics_array = metrics.find_one({"type": "country"}, {"_id": 0})

        if not metrics_array:
            raise HTTPException(status_code=404, detail="Metric Not Found")
        return metrics_array
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Metric Not Found: {str(e)}")

@app.get("/metrics/sign-in")
async def get_sign_in_metrics():
    try:
        metrics_array = metrics.find_one({"type": "sign_in"}, {"_id": 0})

        if not metrics_array:
            raise HTTPException(status_code=404, detail="Metric Not Found")
        return metrics_array
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Metric Not Found: {str(e)}")
