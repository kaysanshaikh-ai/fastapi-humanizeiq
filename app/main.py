# app/main.py
from fastapi import FastAPI
import os

USERNAME = os.getenv("USERNAME", "default_user")
app = FastAPI()

@app.get("/" + USERNAME + "/test")
def read_test():
    return {"username": USERNAME}

@app.get("/health")
def health_check():
    return {"status": "ok"}
