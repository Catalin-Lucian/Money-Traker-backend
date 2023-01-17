from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.auth import auth_handler
from dto.models import UserRegister, UserLogin, DepositAdd, DepositOut
from database.db_manager import SessionLocal, Deposit


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_deposits(user_id: int = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    return db.query(Deposit).filter(Deposit.user_id == user_id).all()


def add_deposit(deposit: DepositAdd, user_id: int = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    new_deposit = Deposit(amount=deposit.amount, user_id=user_id, name=deposit.name)
    db.add(new_deposit)
    db.flush()
    db.commit()

    deposit_out = DepositOut(id=new_deposit.id, amount=new_deposit.amount,
                             name=new_deposit.name, ico_name=new_deposit.ico_name)
    return deposit_out


def delete_deposit(deposit_id: int, user_id: int = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    db.query(Deposit).filter(Deposit.id == deposit_id).delete()
    db.commit()

    return {"message": "deleted successfully"}
