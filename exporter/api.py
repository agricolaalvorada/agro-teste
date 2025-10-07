from fastapi import APIRouter, HTTPException, FastAPI
from pydantic import BaseModel
from typing import Any
import os
import uvicorn

router = APIRouter()

class TelemetryRequest(BaseModel):
    operation: str
    duration: int  # timestamp in milliseconds
    placa: str
    timestamp: int  # timestamp in milliseconds
    identifier: str

@router.post("/telemetry")
async def receive_telemetry(data: TelemetryRequest) -> Any:

    return {"status": "success"}


@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    
    uvicorn.run("api:app", host="0.0.0.0", port=8089)
