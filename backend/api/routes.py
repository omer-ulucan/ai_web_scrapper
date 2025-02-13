from fastapi import APIRouter, Query
from backend.services import scraper, categorization, optimizer, ai, noise_reduction
from backend.rl_agent import rl_scraper

router = APIRouter()

@router.get("/scrape")
async def scrape(query: str = Query(..., description="Search query (e.g., brain_tumor)")):
    # Trigger the web scraping process using the provided query.
    data = await scraper.scrape(query)
    return {"status": "success", "data": data}