from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile

main_app = FastAPI()

@main_app.get("/")
async def root():
    return {"message": "response"}
