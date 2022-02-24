from fastapi import APIRouter
from api_functions import ResponseModel, ErrorResponseModel
import geocoder

router = APIRouter()


@router.get('/reverse',
        name="Reverse Geocoding",
        description="Returns the address of given geographical coordinates")
async def reverse(lat: float, lon: float):
    """Returns the address of a given geographical coordinates"""
    try:
        geolocator = geocoder.osm([lat, lon], method='reverse')
        address = geolocator.json['raw']['display_name']
        data = {
            "source": "OSM",
            "longitude": lon,
            "latitude": lat,
            "address": address
        }
        return ResponseModel(data, "success")
    except Exception:
        return ErrorResponseModel(503, "Internal Server Error")

