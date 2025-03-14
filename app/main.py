from typing import Annotated
from uuid import UUID, uuid4
from fastapi import Body, FastAPI
from dotenv import load_dotenv
import os
from pydantic import BaseModel, AfterValidator, IPvAnyAddress
from contextlib import asynccontextmanager

from .routers import api_v1

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     pass
#     yield
#     pass

app = FastAPI()
app.include_router(api_v1.router)

load_dotenv()

@app.get("/")
async def root():
    return {"message": "..."}

