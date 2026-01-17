from fastapi import APIRouter

from .main import create_order
from .schemas import CreateOrderRequest, CreateOrderResponse

router = APIRouter()


@router.post("/orders", response_model=CreateOrderResponse)
def create_order_route(req: CreateOrderRequest) -> CreateOrderResponse:
    create_order(req.order_id)
    return CreateOrderResponse(status="ok")
