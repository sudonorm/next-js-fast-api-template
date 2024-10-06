from fastapi import FastAPI, responses
from fastapi.routing import APIRoute

from fastapi.middleware.cors import CORSMiddleware as CORSMiddleware

from fastapi.staticfiles import StaticFiles

import sys
import os

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


if home_dir not in sys.path:
    sys.path.append(home_dir)

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

if f'{parent_dir}{os.sep}{"db"}' not in sys.path:
    sys.path.append(f'{parent_dir}{os.sep}{"db"}')

import logging

### Only import after appending the paths appropriately
from app.api.api_v1.api import api_router
from app.core.config import settings

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


### In production, consider disabling /docs and /redoc by uncommenting the last two lines in the 'app' initialization below
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    default_response_class=responses.ORJSONResponse,
    # docs_url=None,
    # redoc_url=None,
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
