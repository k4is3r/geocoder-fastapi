from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()

@router.get("/",
        name="Home Page",
        description="API documentation Page")
async def main():
    """API documentation Page"""
    return RedirectResponse(url="/docs")

