"""
calculator.py
-------------
Simple Calculator — Target application for Automated Test Case Generator.

Provides four basic arithmetic operations with explicit input validation
and error handling. All functions use type hints for clarity.
"""


def add(a: float, b: float) -> float:
    """
    Return the sum of a and b.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: The result of a + b.

    Raises:
        TypeError: If either a or b is not a numeric type (int or float).

    Examples:
        >>> add(3, 5)
        8
        >>> add(-1, 1)
        0
        >>> add(0.1, 0.2)
        0.30000000000000004
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError(f"Operand 'a' must be a number, got {type(a).__name__}.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError(f"Operand 'b' must be a number, got {type(b).__name__}.")
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Return the difference of a and b (a - b).

    Args:
        a (float): Minuend.
        b (float): Subtrahend.

    Returns:
        float: The result of a - b.

    Raises:
        TypeError: If either a or b is not a numeric type (int or float).

    Examples:
        >>> subtract(10, 4)
        6
        >>> subtract(0, 5)
        -5
        >>> subtract(-3, -3)
        0
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError(f"Operand 'a' must be a number, got {type(a).__name__}.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError(f"Operand 'b' must be a number, got {type(b).__name__}.")
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Return the product of a and b.

    Args:
        a (float): First factor.
        b (float): Second factor.

    Returns:
        float: The result of a * b.

    Raises:
        TypeError: If either a or b is not a numeric type (int or float).

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 5)
        -10
        >>> multiply(0, 999)
        0
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError(f"Operand 'a' must be a number, got {type(a).__name__}.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError(f"Operand 'b' must be a number, got {type(b).__name__}.")
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of a divided by b (a / b).

    Args:
        a (float): Dividend.
        b (float): Divisor.

    Returns:
        float: The result of a / b.

    Raises:
        TypeError:   If either a or b is not a numeric type (int or float).
        ValueError:  If b is zero (division by zero is not allowed).

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(-9, 3)
        -3.0
        >>> divide(1, 3)
        0.3333333333333333
        >>> divide(5, 0)
        ValueError: Cannot divide by zero.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError(f"Operand 'a' must be a number, got {type(a).__name__}.")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError(f"Operand 'b' must be a number, got {type(b).__name__}.")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
