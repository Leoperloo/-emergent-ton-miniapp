from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="TON Crowdfunding MiniApp API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For Telegram MiniApp
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client.ton_crowdfunding

@app.get("/")
async def root():
    return {"message": "TON Crowdfunding MiniApp Backend is running!"}

# Import routers later
# from routers import users, projects, etc.

print("Backend initialized")
