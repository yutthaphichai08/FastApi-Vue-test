import csv
import io
from typing import List
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

import crud, models, schemas,middleware
from db import conn, engine
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
    'http://127.0.0.1:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
     middleware.AuthenMiddleware
)

@app.post("/application", response_model=schemas.Application)
def create_user(appli: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    # ตรวจสอบว่ามีการส่ง firstname และ lastname มาหรือไม่
    if not appli.firstname or not appli.lastname:
        raise HTTPException(status_code=400, detail="Firstname and Lastname are required")

    return crud.create_appli(db=db, appli=appli)


@app.get("/admin/application", response_model=list[schemas.Application])
def read_applis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    applis = crud.get_applis(db, skip=skip, limit=limit)
    return applis


@app.get("/admin/application/{appli_id}", response_model=schemas.Application)
def get_appli(appli_id: int, db: Session = Depends(get_db)):
    db_appli= crud.get_appli(db=db, appli_id=appli_id)
    if not db_appli:
        raise HTTPException(status_code=404, detail="Application not found")
    return db_appli


@app.put("/admin/application/update/{appli_id}", response_model=schemas.Application)
def appli_update(appli_id: int, appli_update: schemas.ApplicationUpdate, db: Session = Depends(get_db)):
    if not appli_update.firstname or not appli_update.lastname:
        raise HTTPException(status_code=400, detail="Firstname and Lastname are required")

    db_appli = crud.update_appli(db=db, appli_id=appli_id, appli_update=appli_update)
    if not db_appli:
        raise HTTPException(status_code=404, detail="Application not found")
    return db_appli


@app.delete("/admin/application/{appli_id}", response_model=schemas.Application)
def de_activate_user(appli_id: int, db: Session = Depends(get_db)):
    db_appli = crud.delete_appli(db=db, appli_id=appli_id)
    if not db_appli:
        raise HTTPException(status_code=404, detail="Application not found")
    return db_appli

    
@app.get("/admin/export")
async def export_users(db: Session = Depends(get_db)):
    applis = crud.get_applis(db)
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "firstname", "lastname","address","salary","is_active"])
    
    for appli in applis:
        writer.writerow([appli.id, appli.firstname, appli.lastname,appli.address,appli.salary,appli.is_active])
    
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=users.csv"
    })
    

@app.post("/admin/import")
async def update_applis_from_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):

    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    contents = await file.read()
    csv_reader = csv.reader(io.StringIO(contents.decode("utf-8")))

    # remove header
    header = next(csv_reader)

    updated_applis = crud.import_appli(db, csv_reader)

    return {"detail": "updated successfully", "updated_data": updated_applis}


#------------------------------------------------------------------------------------------------


@app.post('/login', response_model=schemas.UserToken)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    login_user = crud.login_user(db, email=user.email, password=user.password)
    return login_user


@app.get("/admin/users", response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.post('/users', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db=db, user=user)


