# order-service

Manages order lifecycle including creation and tracking.

## Why this repo exists

Order management is a core business capability that requires its own service for handling complex order state transitions and business logic.

## Core Components

### `create_order(order_id: str)`
Creates a new order in the system.

**Logs:**
- `order_created` — Logged when an order is successfully created, includes the order ID
