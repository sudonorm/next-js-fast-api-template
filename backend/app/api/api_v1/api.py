from fastapi import APIRouter
from app.api.api_v1.endpoints import swagger_docs, users, items

api_router = APIRouter()

api_router.include_router(swagger_docs.router, prefix="/docs", tags=["docs"])

api_router.include_router(users.router, prefix="/users", tags=["users"])

api_router.include_router(items.router, prefix="/items", tags=["items"])