from core_logger import get_logger

logger = get_logger("order-service")


def create_order(order_id: str) -> None:
    logger.info("order_created", order_id=order_id)


def main() -> None:
    create_order("order-001")


if __name__ == "__main__":
    main()
