import csv
import io
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

import crud, models, schemas
from database import conn, engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = conn()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # ตรวจสอบว่ามีการส่ง firstname และ lastname มาหรือไม่
    if not user.firstname or not user.lastname:
        raise HTTPException(status_code=400, detail="Firstname and Lastname are required")

    return crud.create_user(db=db, user=user)


@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/user/update/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    if not user_update.firstname or not user_update.lastname:
        raise HTTPException(status_code=400, detail="Firstname and Lastname are required")

    db_user = crud.update_user(db=db, user_id=user_id, user_update=user_update)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.patch("/user/delete/{user_id}", response_model=schemas.User)
def de_activate_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/export")
async def export_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "firstname", "lastname","address","salary","is_active"])
    
    for user in users:
        writer.writerow([user.id, user.firstname, user.lastname,user.address,user.salary,user.is_active])
    
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=users.csv"
    })

@app.post("/import")
async def update_users_from_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):

    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    contents = await file.read()
    csv_reader = csv.reader(io.StringIO(contents.decode("utf-8")))

    # remove header
    header = next(csv_reader)

    updated_users = crud.import_user(db, csv_reader)

    return {"detail": "updated successfully", "updated_data": updated_users}



