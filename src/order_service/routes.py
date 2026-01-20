"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import create_order
from .schemas import CreateOrderRequest, CreateOrderResponse

router = APIRouter()


@router.post("/orders", response_model=CreateOrderResponse)
def create_order_route(req: CreateOrderRequest) -> CreateOrderResponse:
    create_order(req.order_id)
    return CreateOrderResponse(status="ok")
