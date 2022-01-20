import traceback
from typing import Dict, List
import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from schema import CompanyRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ionic_api_log")

@app.get('/')
def hello() -> Dict:
    return {"message": "hello"}

@app.get('/city', response_model=List)
def crawl() -> List:
    try:
        city = []
        for i in range(1, 48):
            params = {
                'area': str(i).zfill(2)
            }
            res = requests.get("https://www.land.mlit.go.jp/webland/api/CitySearch", params=params)
            city.append(res.text)

        return city
    except BaseException as e:
        logger.info(f"city_呼び出し失敗\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="city_呼び出し失敗")

@app.post('/company')
def crawl(request: CompanyRequest) -> Dict:
    try:
        params = {
            'appid': "dj00aiZpPUs1T0FIdXlTWFhrTyZzPWNvbnN1bWVyc2VjcmV0Jng9MmE-",
            "localGovernmentCode": request.id,
        }
        res = requests.get("https://job.yahooapis.jp/v1/furusato/company/", params=params)

        return res.content
    except BaseException as e:
        logger.info(f"company_呼び出し失敗\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="company_呼び出し失敗")

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)
