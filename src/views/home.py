from fastapi import APIRouter
from src.controllers.home_services import home_api

home_route = APIRouter(tags=["home"])


@home_route.get("/")
def home():

    return home_api()
