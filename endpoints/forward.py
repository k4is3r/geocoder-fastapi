from fastapi import APIRouter
from api_functions import ResponseModel, ErrorResponseModel
import geocoder

router = APIRouter()

@router.get("/forward", 
        name="Forward geocoding",
        description="Returns latitude and longitud of a given address.")
async def forward(address: str):
    """ Returns latitude and longitud from a given address """
    try:
        geolocator = geocoder.osm(address)
        address = geolocator.json['raw']['display_name']
        lat = geolocator.json['raw']['lat']
        lon = geolocator.json['raw']['lon']
        data = {
            "source": "OSM",
            "longitude": lon,
            "latitude": lat,
            "address": address,
        }
        return ResponseModel(data, "success")
    except Execption:
        return ErrorResponseModel(503, "Internal Server Error")
