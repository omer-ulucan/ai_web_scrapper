from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def test(name: str):
    return {"message": "AI Web Scrapper API is running"}