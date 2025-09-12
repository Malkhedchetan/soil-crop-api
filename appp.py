from fastapi import FastAPI
from pydantic import BaseModel
import ro

app = FastAPI()

class SoilRequest(BaseModel):
    soil_type: str
    N: float
    P: float
    K: float

class FertilizerRequest(BaseModel):
    soil_type: str
    N: float
    P: float
    K: float
    crop: str

@app.post("/recommend_crop")
def api_recommend_crop(request: SoilRequest):
    result = ro.recommend_best_crop(
        request.soil_type, request.N, request.P, request.K
    )
    return result

@app.post("/fertilizer_plan")
def api_fertilizer_plan(request: FertilizerRequest):
    plan = ro.recommend_fertilizer_for_other_crop(
        request.crop, request.soil_type, request.N, request.P, request.K
    )
    return plan
