import json
import re
import requests
from fastapi import status
from fastapi.responses import JSONResponse
from src.core.config import settings


def get_total_page():
    res = requests.get(settings.TASK_API_ENDPOIN)
    data = res.text
    data = json.loads(data)

    return data["data"]["last_page"]


def extract_links_from_contex(content: str):
    url_pattern = r"https?://[^\s\)]+"

    urls = re.findall(url_pattern, content)
    return urls


def get_citation_api():

    citations = []
    page_no = 1

    while page_no != get_total_page() + 1:

        res = requests.get(f"{settings.TASK_API_ENDPOIN}?page={page_no}")
        text_data = res.text
        page_data = json.loads(text_data)

        for resource in page_data["data"]["data"]:

            for source in resource["source"]:

                if source["link"] != "":
                    citations.append({"id": source["id"], "link": source["link"]})

        print(f"page_no: {page_data['data']['current_page']} fetched")
        page_no += 1

    return JSONResponse(
        content={"citations": citations}, status_code=status.HTTP_200_OK
    )
