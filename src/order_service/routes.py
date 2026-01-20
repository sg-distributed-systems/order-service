"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import CreateOrderRequest, CreateOrderResponse
from .service import create_order

router = APIRouter()


@router.post("/orders", response_model=CreateOrderResponse, status_code=200)
def create_order_route(req: CreateOrderRequest) -> CreateOrderResponse:
    result = create_order(
        customer_id=req.customer_id,
        items=req.items,
        shipping_address=req.shipping_address,
    )
    return CreateOrderResponse(
        order_id=result["order_id"],
        status=result["status"],
        total=result["total"],
        created_at=result["created_at"],
    )
