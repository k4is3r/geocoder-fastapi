from fastapi import APIRouter
from endpoints import home_page, reverse, forward, ip_address

router = APIRouter()

router.include_route(home_page.router, tags=["Home"])
router.include_route(reverse.router, tags=["Reverse"])
router.include_route(forward.router, tags=["Forward"])
router.include_route(ip_address.route, tags=["IP_Address"])

