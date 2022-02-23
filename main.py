from fastapi import FastAPI
from routers import router

app = FastAPI(
        title="KasierGeocoder",
        description="A simple geocoding API seervice built with FastAPI",
        version="0.001"
)

app.include_router(router)

