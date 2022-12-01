from pydantic import BaseModel, EmailStr, conint, Field
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

    
class PostCreate(PostBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    
class UserOut(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

        
class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True


class PostOut(BaseModel):
    post: PostResponse = Field(alias='Post')
    votes: int
    
    class Config:
        orm_mode = True


    
class Token(BaseModel):
    access_token: str
    token_type: str


    
class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1, ge=0)