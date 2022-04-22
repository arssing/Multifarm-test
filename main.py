from fastapi import FastAPI
from utils import get_APR

app = FastAPI()

@app.get("/")
async def root():
    try:
        apr = get_APR()
        return {"apr":apr}
    except:
        return {"error":"something went wrong"}