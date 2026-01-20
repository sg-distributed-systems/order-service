"""
Service entrypoint with lifecycle management.

Initializes configuration, correlation ID, and signal handlers before running
the main service logic. Provides structured error handling for all exceptions.
"""
from core_logger import get_logger

from order_service.config import load_config
from order_service.errors import AppError
from order_service.lifecycle import install_signal_handlers
from order_service.observability import init_correlation_id

logger = get_logger("order-service")


def create_order(order_id: str) -> None:
    logger.info("order_created", order_id=order_id)


def run() -> None:
    cfg = load_config("order-service")
    cid = init_correlation_id()
    install_signal_handlers("order-service")

    logger.info("service_starting", env=cfg.env, correlation_id=cid)

    try:
        create_order("order-001")
        logger.info("service_completed")
    except AppError as e:
        logger.warning("app_error", **e.to_log_fields())
        raise
    except Exception as e:
        logger.exception("unhandled_exception", exc=e)
        raise


def main() -> None:
    run()


if __name__ == "__main__":
    main()
