from fastapi import APIRouter
from src.controllers.citations_services import get_citation_api

citation_route = APIRouter(tags=["Citation"])


@citation_route.get("/get_citation")
def get_citation():

    return get_citation_api()
