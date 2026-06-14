from fastapi import FastAPI
from runner import run_factory

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/run")
def run():
    return {"result": run_factory()}
