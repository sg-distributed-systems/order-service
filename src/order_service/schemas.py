from pydantic import BaseModel


class CreateOrderRequest(BaseModel):
    order_id: str


class CreateOrderResponse(BaseModel):
    status: str
