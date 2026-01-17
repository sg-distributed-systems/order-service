# order-service

Manages order lifecycle including creation and tracking.

## Why this repo exists

Order management is a core business capability that requires its own service for handling complex order state transitions and business logic.

## Core Components

### `create_order(order_id: str)`
Creates a new order in the system.

**Logs:**
- `order_created` — Logged when an order is successfully created, includes the order ID

## HTTP Interface

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe |
| `/readyz` | GET | Readiness probe |
| `/orders` | POST | Creates a new order |

### Running the service

```bash
uvicorn src.order_service.app:app --host 0.0.0.0 --port 8003
```
