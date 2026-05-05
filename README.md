# Task Manager API

This is a backend project built using FastAPI.

## Features
- User Registration
- User Login
- CRUD Operations (Create, Read, Update, Delete Tasks)

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run server:
uvicorn main:app --reload

3. Open browser:
http://127.0.0.1:8000/docs

## API Endpoints
- POST /register
- POST /login
- GET /tasks
- POST /tasks
- PUT /tasks/{id}
- DELETE /tasks/{id}
