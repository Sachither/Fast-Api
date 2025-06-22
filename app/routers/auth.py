from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm   
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.oauth2 import create_access_token
# from app.schemas import UserLogin
from app.utils import verify_password

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", response_model=schemas.Token)
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    if not db_user or not verify_password(user_credential.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            # invalid credentials is better than user with email not found for security reasons
            detail=f"invalid credentials"
        )
        
    # Here you would typically create a JWT token or session token
    access_token = create_access_token(data ={"user_id": db_user.id})

    return {"access_token": access_token, "token_type": "bearer"}
