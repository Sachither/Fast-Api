import datetime
from typing import Annotated, Literal, Optional
from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime.datetime
    
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(PostBase):
    pass

class PostVote(BaseModel):
    post: 'PostResponse'
    votes: int
    
    class Config:
        from_attributes = True

class PostResponse(PostBase):
    id: int
    created_at: datetime.datetime
    owner_id: int
    owner: UserResponse
    
    class Config:
        from_attributes = True
    
class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserCreate(UserBase):
    pass

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[int] = None
    
class Vote(BaseModel):
    post_id: int
    # direction: Annotated[int, Field(strict=True, le=1)] 
    direction: Literal[0, 1]  # Only allows 0 or 1
