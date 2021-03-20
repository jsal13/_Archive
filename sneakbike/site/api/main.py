from typing import Optional, List
import json

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from hkr_quick_seed_tracker import DreamerSpoiler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HKRSpoilerUpload(BaseModel):
    files: str


@app.post("/api/hkr/uploadspoiler/")
async def hkr_upload_spoiler(data: HKRSpoilerUpload):
    ds = DreamerSpoiler(data.files)

    payload = {
        "dreamers": ds.dreamers,
        "abilities": ds.main_abilities,
        "useful_items": ds.useful_items,
    }

    return payload

