from fastapi import FastAPI
from src.views import home,citations

app = FastAPI(title="BeyondChats Task")

app.include_router(home.home_route)
app.include_router(citations.citation_route)
