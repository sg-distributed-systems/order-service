"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    sku: str
    quantity: int = Field(gt=0)
    unit_price: Decimal = Field(gt=0)


class Address(BaseModel):
    street: str
    city: str
    state: Optional[str] = None
    postal_code: str
    country: str


class CreateOrderRequest(BaseModel):
    customer_id: str
    items: List[OrderItem]
    shipping_address: Address


class CreateOrderResponse(BaseModel):
    order_id: UUID
    status: str
    total: Decimal
    created_at: datetime
