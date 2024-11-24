import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

# Database Setup
from app.db.session import init_db

# Router
from app.api import example, chat, search, user

load_dotenv()
# init_db() # DB 생성

# FastAPI WEB 서버
app = FastAPI()
# app.mount("/backend/public", StaticFiles(directory="public"), name="public")

# Router
app.include_router(example.router)
app.include_router(chat.router)
app.include_router(search.router)
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run(app, port=8000, timeout_keep_alive=90)
