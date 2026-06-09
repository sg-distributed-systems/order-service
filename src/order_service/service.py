"""
Order processing and lifecycle management.

Handles order creation, validation, pricing calculation, and status transitions.
Manages order items, shipping addresses, and coordinates with inventory and
payment services.
"""
from datetime import datetime
from decimal import Decimal
from typing import List
from uuid import uuid4

from core_logger import get_logger

from .errors import ValidationError
from .schemas import Address, OrderItem

logger = get_logger("order-service", tier="compliance")


def create_order(
    customer_id: str, items: List[OrderItem], shipping_address: Address
) -> dict:
    logger.info(
        "order_creation_started", customer_id=customer_id, item_count=len(items)
    )

    if not items:
        raise ValidationError("order_must_have_items")

    total = Decimal("0")
    for item in items:
        if item.quantity <= 0:
            raise ValidationError("invalid_item_quantity", details={"sku": item.sku})
        if item.unit_price <= 0:
            raise ValidationError("invalid_item_price", details={"sku": item.sku})
        total += item.unit_price * item.quantity
        logger.debug(
            "item_added",
            sku=item.sku,
            quantity=item.quantity,
            line_total=str(item.unit_price * item.quantity),
        )

    order_id = uuid4()

    if not shipping_address.postal_code:
        raise ValidationError("postal_code_required")

    logger.info(
        "order_created", order_id=str(order_id), customer_id=customer_id, total=str(total)
    )
    return {
        "order_id": order_id,
        "status": "pending",
        "total": total,
        "created_at": datetime.utcnow(),
    }


def cancel_order(order_id: str, reason: str) -> dict:
    logger.info("order_cancellation", order_id=order_id, reason=reason)
    return {"order_id": order_id, "status": "cancelled", "cancelled_at": datetime.utcnow()}


def apply_discount_code(order_id: str, code: str, subtotal: Decimal) -> Decimal:
    logger.info("discount_code_applied", order_id=order_id, code=code)

    if not code:
        raise ValidationError("discount_code_required")

    discount = Decimal("0.10") if code.upper().startswith("SAVE") else Decimal("0")
    adjusted = subtotal * (Decimal("1") - discount)

    logger.debug(
        "discount_calculated",
        order_id=order_id,
        discount=str(discount),
        adjusted_total=str(adjusted),
    )
    return adjusted
