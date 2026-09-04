import logging

logger = logging.getLogger(__name__)

MAX_RETRIES = 3

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def divide(a: int, b: int) -> float:
    """Return a divided by b."""
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("division by zero")
        return 0.0
