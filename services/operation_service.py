from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.auth import auth_handler
from database.db_manager import SessionLocal, Deposit, Operation

from dto.models import OperationOut


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_operations(page: int, nr_per_page: int, user_id: int = Depends(auth_handler.auth_wrapper),
                   db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    # get all operations for the page ordered by date descending
    operations = db.query(Operation).filter(Operation.user_id == user_id).order_by(Operation.date.desc()) \
        .offset(page * nr_per_page).limit(nr_per_page).all()

    # turn the operations into OperationOut objects with the deposit name
    operations_out = []
    for operation in operations:
        deposit = db.query(Deposit).filter(Deposit.id == operation.deposit_id).first()
        operations_out.append(OperationOut(id=operation.id, amount=operation.amount, date=operation.date,
                                           deposit_name=deposit.name))

    return operations_out
