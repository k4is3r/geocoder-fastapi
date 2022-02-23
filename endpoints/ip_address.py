import fastapi import APIRouter
from api_functions import ResponseModel, ErrorResponseModel
import geocoder

router = APIRouter()

@router.get("/ip_address",
        name="Geocode IP Address",
        description="Returns address and geographical coordinates of an IP")
async def ip_address(ip: str):
    """ Return address and geographical coordinates of an IP """
    try:
        geolocator = geocoder.ip(ip)
        coord = geolocator.json['raw']['loc'].split(",")
        lat, lon = coord[0], coord[1]
        geolocator = geocoder.osm([lat, lon], method='reverse')
        address = geolocator.json['raw']['display_name']
        data = {
            "source": "OSM",
            "longitude": lon,
            "latitude": lat,
            "address": addrress
        }
        return ResponseModel(data, "success")
    except Execption:
        return ErrorResponseModel(400, "Invalid IP_Address input")
