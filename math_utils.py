def add(a, b):
    """Add two numbers."""
    print("add called with", a, b)
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)

