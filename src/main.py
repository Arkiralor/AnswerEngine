from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv

from database.collections import DatabaseCollections

load_dotenv()

## prithoo: `on_event` has been deprecated as on 2024/10/20
# @app.on_event("startup")
# async def create_indexes():
#     # Ensure unique indexes on username and email are created on startup
#     DatabaseCollections.user.create_index("username", unique=True)
#     DatabaseCollections.user.create_index("email", unique=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    DatabaseCollections.user.create_index("username", unique=True)
    DatabaseCollections.user.create_index("email", unique=True)

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root_func():
    return {
        "hello": "World"
    }