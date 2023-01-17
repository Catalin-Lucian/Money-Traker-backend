from datetime import datetime

from pydantic import BaseModel


class UserRegister(BaseModel):
    name: str
    email: str
    password: str
    confirmPassword: str


class UserLogin(BaseModel):
    email: str
    password: str


class DepositAdd(BaseModel):
    name: str
    amount: float


class DepositOut(BaseModel):
    id: int
    name: str
    amount: float
    ico_name: str


class OperationOut(BaseModel):
    id: int
    name: str
    amount: float
    ico_name: str
    date: datetime
