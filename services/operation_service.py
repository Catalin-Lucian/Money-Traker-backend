from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.auth import auth_handler
from database.db_manager import SessionLocal, Deposit, Operation

from dto.models import OperationOut, OperationAdd


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_operations(page: int, perPage: int, user_id: int = Depends(auth_handler.auth_wrapper),
                   db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    # get all operations for the page ordered by date descending
    operations = db.query(Operation).filter(Operation.user_id == user_id).order_by(Operation.date.desc()).offset(
        (page - 1) * perPage).limit(perPage).all()

    # turn the operations into OperationOut objects with the deposit name
    operations_out = []
    for operation in operations:
        deposit = db.query(Deposit).filter(Deposit.id == operation.deposit_id).first()
        operations_out.append(OperationOut(id=operation.id, amount=operation.amount, date=operation.date,
                                           name=deposit.name, ico_name=''))

    return operations_out


def get_operation_by_id(deposit_id: int, page: int, perPage: int,
                        user_id: int = Depends(auth_handler.auth_wrapper),
                        db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")


    # get all operations for the page ordered by date descending
    operations = db.query(Operation) \
        .filter(Operation.user_id == user_id) \
        .filter(Operation.deposit_id == deposit_id) \
        .order_by(Operation.date.desc()).offset(
        (page - 1) * perPage).limit(perPage).all()

    # turn the operations into OperationOut objects with the deposit name
    operations_out = []
    for operation in operations:
        deposit = db.query(Deposit).filter(Deposit.id == operation.deposit_id).first()
        operations_out.append(OperationOut(id=operation.id, amount=operation.amount, date=operation.date,
                                           name=deposit.name, ico_name=''))

    return operations_out


def add_operation(operationAdd: OperationAdd, user_id: int = Depends(auth_handler.auth_wrapper),
                  db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    # get the deposit
    deposit = db.query(Deposit).filter(Deposit.id == operationAdd.deposit_id).first()

    # check if the deposit belongs to the user
    if deposit.user_id != user_id:
        raise HTTPException(status_code=400, detail="Invalid deposit")

    # add the operation
    new_operation = Operation(amount=operationAdd.amount, deposit_id=operationAdd.deposit_id, user_id=user_id)
    db.add(new_operation)
    db.flush()
    db.commit()

    # get the deposit name
    deposit = db.query(Deposit).filter(Deposit.id == new_operation.deposit_id).first()

    # update the deposit amount
    deposit.amount += new_operation.amount
    db.commit()

    # return the operation
    return OperationOut(id=new_operation.id, amount=new_operation.amount, date=new_operation.date,
                        name=deposit.name, ico_name='')


def delete_operation(operation_id: int, user_id: int = Depends(auth_handler.auth_wrapper),
                     db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid token")

    # get the operation
    operation = db.query(Operation).filter(Operation.id == operation_id).first()

    # check if the operation belongs to the user
    if operation.user_id != user_id:
        raise HTTPException(status_code=400, detail="Invalid operation")

    # get the deposit
    deposit = db.query(Deposit).filter(Deposit.id == operation.deposit_id).first()

    # update the deposit amount
    deposit.amount -= operation.amount
    db.commit()

    # delete the operation
    db.query(Operation).filter(Operation.id == operation_id).delete()
    db.commit()

    return {"message": "deleted successfully"}
