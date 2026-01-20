"""
Service entrypoint for the order-service.

This module serves as the application entry point, responsible solely for
initializing and running the uvicorn ASGI server. All business logic is
contained in service.py; this file handles only server configuration and startup.

Usage:
    python -m order_service.main
"""
import uvicorn

from order_service.app import app
from order_service.config import load_config


def main() -> None:
    cfg = load_config("order-service")
    uvicorn.run(app, host="0.0.0.0", port=cfg.port)


if __name__ == "__main__":
    main()
