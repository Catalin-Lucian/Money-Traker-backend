import services.deposit_service as deposit_service
from fastapi import APIRouter, Depends

from dto.models import DepositOut

deposits = APIRouter()


@deposits.get("/api/deposits", status_code=200)
async def get_deposits(res: dict = Depends(deposit_service.get_deposits)):
    return res


@deposits.post("/api/deposits", status_code=201)
async def add_deposit(res: DepositOut = Depends(deposit_service.add_deposit)):
    return res


@deposits.delete("/api/deposits/{deposit_id}", status_code=200)
async def delete_deposit(res: dict = Depends(deposit_service.delete_deposit)):
    return res
