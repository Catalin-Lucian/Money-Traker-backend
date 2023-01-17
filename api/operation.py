import services.operation_service as operation_service
from fastapi import APIRouter, Depends

operations = APIRouter()


@operations.get("/api/operations", status_code=200)
async def get_operations(res=Depends(operation_service.get_operations)):
    return res
