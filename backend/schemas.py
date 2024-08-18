from typing import Optional
from pydantic import BaseModel


# สร้าง Schema สำหรับสร้าง User
class UserCreate(BaseModel):
    firstname: str
    lastname: str
    address: str
    salary: int
    is_active: bool = True  

# Schema สำหรับการอัปเดตผู้ใช้
class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    address: Optional[str] = None
    salary: Optional[int] = 0
    is_active: Optional[bool] = None

# สร้าง Schema สำหรับการแสดงผล User
class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    address: str
    salary: int
    is_active: bool

    class Config:
        from_attributes = True

# สร้าง Schema สำหรับการลบ User
class DeleteUser(BaseModel):
    is_active: bool = False  


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool

#     class Config:
#         from_attributes = True