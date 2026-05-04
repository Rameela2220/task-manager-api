from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

# DB
def get_db():
    return next(database.get_db())

# =========================
# USER APIs (OLD STYLE)
# =========================

@app.post("/register")
def register(name: str, email: str, password: str, db: Session = Depends(get_db)):

    existing = db.query(models.User).filter(models.User.email == email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = models.User(name=name, email=email, password=password)

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created"}


@app.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password != password:
        raise HTTPException(status_code=400, detail="Wrong password")

    return {"message": "Login successful"}

# =========================
# TASK APIs (CRUD)
# =========================

@app.post("/tasks")
def create_task(title: str, description: str, db: Session = Depends(get_db)):

    task = models.Task(title=title, description=description)

    db.add(task)
    db.commit()
    db.refresh(task)

    return {"message": "Task created"}


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, description: str, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = title
    task.description = description

    db.commit()

    return {"message": "Task updated"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}