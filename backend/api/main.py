from fastapi import FastAPI
from .routes import router
import uvicorn

app = FastAPI(title="AI Webscraper API", version="1.0")

# Include API routes
app.include_router(router)

if __name__ == "__main__":
    # Run the application on host 0.0.0.0 and port 8000 with auto-reload enabled
    uvicorn.run("backend.api.main:app", host="0.0.0.0", port=8000, reload=True)