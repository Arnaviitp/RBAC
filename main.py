from fastapi import FastAPI, UploadFile, Depends, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
from utils import parse_delivery_file
from services import save_orders, get_orders
from auth import create_jwt_token
from datetime import timedelta

# Database Setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Login API
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "vendor" and password == "password":
        token = create_jwt_token({"sub": username}, timedelta(hours=2))
        return {"access_token": token}
    return {"error": "Invalid credentials"}

# Upload API
@app.post("/upload")
async def upload_file(file: UploadFile, db: Session = Depends(get_db)):
    content = await file.read()
    orders = parse_delivery_file(content.decode())
    save_orders(db, orders)
    return {"status": "File processed successfully"}

# Get Orders API
@app.get("/orders")
def list_orders(vendor_name: str, date: str = None, db: Session = Depends(get_db)):
    orders = get_orders(db, vendor_name, date)
    return orders
