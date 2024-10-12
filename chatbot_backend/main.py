from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.conversations import router as conversations_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#include our routes
app.include_router(conversations_router)
