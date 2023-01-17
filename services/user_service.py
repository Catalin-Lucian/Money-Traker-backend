from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.auth import auth_handler
from dto.models import UserRegister, UserLogin
from database.db_manager import User, SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def user_exists(email: str, db: Session = Depends(get_db)):
    """
    Check if a user with the given email already exists in the database.
    """
    return db.query(User).filter(User.email == email).first() is not None


def register_user(data: UserRegister, db: Session = Depends(get_db)):
    """
    Register a new user in the database.
    """
    if user_exists(data.email, db):
        raise HTTPException(status_code=400, detail="This email is already used")
    if data.password != data.confirmPassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    user = User(name=data.name, email=data.email, password= auth_handler.get_password_hash(data.password))
    db.add(user)
    db.commit()

    return {"message": "registered successfully"}


def login_user(data: UserLogin, db: Session = Depends(get_db)):
    if not user_exists(data.email, db):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    user = db.query(User).filter(User.email == data.email).first()
    if auth_handler.verify_password(data.password, user.password):
        token = auth_handler.encode_token(user.id)

        return {"token": token}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")


