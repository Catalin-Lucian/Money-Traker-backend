import services.operation_service as operation_service
from fastapi import APIRouter, Depends

operations = APIRouter()


@operations.get("/api/operations", status_code=200)
async def get_operations(res=Depends(operation_service.get_operations)):
    return res


@operations.get("/api/operations/{deposit_id}", status_code=200)
async def get_operation(res=Depends(operation_service.get_operation_by_id)):
    return res


@operations.post("/api/operations", status_code=200)
async def add_operation(res=Depends(operation_service.add_operation)):
    return res


@operations.delete("/api/operations/{operation_id}", status_code=200)
async def delete_operation(res=Depends(operation_service.delete_operation)):
    return res
