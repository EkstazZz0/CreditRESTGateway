from typing import Annotated
from uuid import UUID

from fastapi import Body, FastAPI

from dotenv import load_dotenv
import os

from pydantic import BaseModel, AfterValidator, IPvAnyAddress

from validate.request_response_models import CreateLoanBid

app = FastAPI()

load_dotenv()

api_url = os.getenv("API_URL") 


@app.get(api_url)
async def main() -> dict:
    
    return {"message": api_url}


@app.post(api_url + "/loan/apply")
async def create_loan(create_loan_bid: CreateLoanBid) -> CreateLoanBid:
    return create_loan_bid


@app.get(api_url + "/loan/status/{loan_id}")
async def get_loan_status(
    loan_id: UUID
) -> dict:
    return {}