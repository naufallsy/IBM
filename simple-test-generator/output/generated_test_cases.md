# Generated Test Cases — Simple Calculator

**Source Analyzed:** `target/calculator.py`  
**Generator:** AI-Powered Automated Test Case Generator (IBM Bob)  
**Total Test Cases:** 40  
**Functions Covered:** `add`, `subtract`, `multiply`, `divide`

---

## Source Code Analysis Summary

| Function | Parameters | Return Type | Raises | Guards |
|---|---|---|---|---|
| `add(a, b)` | float, float | float | TypeError | isinstance check on a, isinstance check on b |
| `subtract(a, b)` | float, float | float | TypeError | isinstance check on a, isinstance check on b |
| `multiply(a, b)` | float, float | float | TypeError | isinstance check on a, isinstance check on b |
| `divide(a, b)` | float, float | float | TypeError, ValueError | isinstance check on a, isinstance check on b, b == 0 check |

**Identified Branches per Function:**
- `add`, `subtract`, `multiply`: 5 branches each (guard-a True, guard-a False, guard-b True, guard-b False, normal return)
- `divide`: 7 branches (same 4 guards + zero-divisor True, zero-divisor False, normal return)

---

## Positive Test Cases

| TC ID | Function | Test Scenario | Preconditions | Input Data | Test Steps | Expected Result | Priority |
|---|---|---|---|---|---|---|---|
| TC-ADD-001 | `add` | Sum of two positive integers | Calculator module imported | a=3, b=5 | 1. Call `add(3, 5)` | Returns `8` | Critical |
| TC-ADD-002 | `add` | Sum of a negative and positive integer | Calculator module imported | a=-1, b=1 | 1. Call `add(-1, 1)` | Returns `0` | Critical |
| TC-ADD-003 | `add` | Sum of two floats | Calculator module imported | a=1.5, b=2.5 | 1. Call `add(1.5, 2.5)` | Returns `4.0` | High |
| TC-ADD-004 | `add` | Sum where one operand is zero | Calculator module imported | a=0, b=7 | 1. Call `add(0, 7)` | Returns `7` | High |
| TC-ADD-005 | `add` | Sum of two negative integers | Calculator module imported | a=-4, b=-6 | 1. Call `add(-4, -6)` | Returns `-10` | High |
| TC-SUB-001 | `subtract` | Difference of two positive integers | Calculator module imported | a=10, b=4 | 1. Call `subtract(10, 4)` | Returns `6` | Critical |
| TC-SUB-002 | `subtract` | Result is zero when operands are equal | Calculator module imported | a=5, b=5 | 1. Call `subtract(5, 5)` | Returns `0` | High |
| TC-SUB-003 | `subtract` | Result is negative when b > a | Calculator module imported | a=3, b=10 | 1. Call `subtract(3, 10)` | Returns `-7` | High |
| TC-SUB-004 | `subtract` | Subtraction with a negative subtrahend | Calculator module imported | a=5, b=-3 | 1. Call `subtract(5, -3)` | Returns `8` | High |
| TC-SUB-005 | `subtract` | Subtraction of two floats | Calculator module imported | a=5.5, b=2.2 | 1. Call `subtract(5.5, 2.2)` | Returns approx `3.3` | Medium |
| TC-MUL-001 | `multiply` | Product of two positive integers | Calculator module imported | a=3, b=4 | 1. Call `multiply(3, 4)` | Returns `12` | Critical |
| TC-MUL-002 | `multiply` | Product involving zero | Calculator module imported | a=0, b=999 | 1. Call `multiply(0, 999)` | Returns `0` | High |
| TC-MUL-003 | `multiply` | Product of negative and positive | Calculator module imported | a=-2, b=5 | 1. Call `multiply(-2, 5)` | Returns `-10` | High |
| TC-MUL-004 | `multiply` | Product of two negative numbers | Calculator module imported | a=-3, b=-3 | 1. Call `multiply(-3, -3)` | Returns `9` | High |
| TC-MUL-005 | `multiply` | Product of two floats | Calculator module imported | a=2.5, b=4.0 | 1. Call `multiply(2.5, 4.0)` | Returns `10.0` | Medium |
| TC-DIV-001 | `divide` | Division with exact integer result | Calculator module imported | a=10, b=2 | 1. Call `divide(10, 2)` | Returns `5.0` | Critical |
| TC-DIV-002 | `divide` | Division resulting in a float | Calculator module imported | a=1, b=3 | 1. Call `divide(1, 3)` | Returns approx `0.3333` | High |
| TC-DIV-003 | `divide` | Division of negative by positive | Calculator module imported | a=-9, b=3 | 1. Call `divide(-9, 3)` | Returns `-3.0` | High |
| TC-DIV-004 | `divide` | Division of negative by negative | Calculator module imported | a=-6, b=-2 | 1. Call `divide(-6, -2)` | Returns `3.0` | High |
| TC-DIV-005 | `divide` | Dividend is zero | Calculator module imported | a=0, b=5 | 1. Call `divide(0, 5)` | Returns `0.0` | High |

---

## Negative Test Cases

| TC ID | Function | Test Scenario | Preconditions | Input Data | Test Steps | Expected Result | Priority |
|---|---|---|---|---|---|---|---|
| TC-ADD-006 | `add` | Operand `a` is a string | Calculator module imported | a="2", b=3 | 1. Call `add("2", 3)` | Raises `TypeError`: "Operand 'a' must be a number, got str." | High |
| TC-ADD-007 | `add` | Operand `b` is a string | Calculator module imported | a=3, b="5" | 1. Call `add(3, "5")` | Raises `TypeError`: "Operand 'b' must be a number, got str." | High |
| TC-ADD-008 | `add` | Operand `a` is None | Calculator module imported | a=None, b=3 | 1. Call `add(None, 3)` | Raises `TypeError`: "Operand 'a' must be a number, got NoneType." | Medium |
| TC-ADD-009 | `add` | Both operands are strings | Calculator module imported | a="a", b="b" | 1. Call `add("a", "b")` | Raises `TypeError` (guard on `a` fires first) | Medium |
| TC-SUB-006 | `subtract` | Operand `a` is a list | Calculator module imported | a=[1,2], b=3 | 1. Call `subtract([1,2], 3)` | Raises `TypeError`: "Operand 'a' must be a number, got list." | Medium |
| TC-SUB-007 | `subtract` | Operand `b` is None | Calculator module imported | a=5, b=None | 1. Call `subtract(5, None)` | Raises `TypeError`: "Operand 'b' must be a number, got NoneType." | Medium |
| TC-MUL-006 | `multiply` | Operand `b` is a dict | Calculator module imported | a=3, b={} | 1. Call `multiply(3, {})` | Raises `TypeError`: "Operand 'b' must be a number, got dict." | Medium |
| TC-DIV-006 | `divide` | Operand `a` is a string | Calculator module imported | a="10", b=2 | 1. Call `divide("10", 2)` | Raises `TypeError`: "Operand 'a' must be a number, got str." | High |
| TC-DIV-007 | `divide` | Operand `b` is a string | Calculator module imported | a=10, b="2" | 1. Call `divide(10, "2")` | Raises `TypeError`: "Operand 'b' must be a number, got str." | High |

---

## Boundary Value Test Cases

| TC ID | Function | Test Scenario | Preconditions | Input Data | Test Steps | Expected Result | Priority |
|---|---|---|---|---|---|---|---|
| TC-ADD-010 | `add` | Both operands are zero | Calculator module imported | a=0, b=0 | 1. Call `add(0, 0)` | Returns `0` | High |
| TC-ADD-011 | `add` | Very large integers | Calculator module imported | a=10**18, b=10**18 | 1. Call `add(1e18, 1e18)` | Returns `2e18` | Medium |
| TC-ADD-012 | `add` | Very small float operands | Calculator module imported | a=1e-15, b=2e-15 | 1. Call `add(1e-15, 2e-15)` | Returns approx `3e-15` | Medium |
| TC-SUB-008 | `subtract` | Both operands are zero | Calculator module imported | a=0, b=0 | 1. Call `subtract(0, 0)` | Returns `0` | High |
| TC-MUL-007 | `multiply` | One operand is 1 (identity) | Calculator module imported | a=99999, b=1 | 1. Call `multiply(99999, 1)` | Returns `99999` | Medium |
| TC-MUL-008 | `multiply` | One operand is -1 (negation) | Calculator module imported | a=42, b=-1 | 1. Call `multiply(42, -1)` | Returns `-42` | Medium |
| TC-DIV-008 | `divide` | Divisor is 1 (identity) | Calculator module imported | a=77, b=1 | 1. Call `divide(77, 1)` | Returns `77.0` | Medium |
| TC-DIV-009 | `divide` | Dividend equals divisor | Calculator module imported | a=5, b=5 | 1. Call `divide(5, 5)` | Returns `1.0` | Medium |
| TC-DIV-010 | `divide` | Divisor just above zero (float) | Calculator module imported | a=1.0, b=1e-10 | 1. Call `divide(1.0, 1e-10)` | Returns `1e10` (large positive float) | Medium |

---

## Edge Cases

| TC ID | Function | Test Scenario | Preconditions | Input Data | Test Steps | Expected Result | Priority |
|---|---|---|---|---|---|---|---|
| TC-ADD-013 | `add` | Boolean `True` rejected as operand `a` | Calculator module imported | a=True, b=3 | 1. Call `add(True, 3)` | Raises `TypeError`: "Operand 'a' must be a number, got bool." | Medium |
| TC-ADD-014 | `add` | Boolean `False` rejected as operand `b` | Calculator module imported | a=3, b=False | 1. Call `add(3, False)` | Raises `TypeError`: "Operand 'b' must be a number, got bool." | Medium |
| TC-SUB-009 | `subtract` | Boolean operand rejected | Calculator module imported | a=True, b=1 | 1. Call `subtract(True, 1)` | Raises `TypeError`: "Operand 'a' must be a number, got bool." | Medium |
| TC-MUL-009 | `multiply` | Float precision: 0.1 × 0.1 | Calculator module imported | a=0.1, b=0.1 | 1. Call `multiply(0.1, 0.1)` | Returns approx `0.01` (use `pytest.approx`) | Medium |
| TC-MUL-010 | `multiply` | Multiplying by zero with float | Calculator module imported | a=0.0, b=3.14 | 1. Call `multiply(0.0, 3.14)` | Returns `0.0` | Medium |
| TC-DIV-011 | `divide` | Boolean `True` as divisor rejected | Calculator module imported | a=10, b=True | 1. Call `divide(10, True)` | Raises `TypeError`: "Operand 'b' must be a number, got bool." | Medium |
| TC-DIV-012 | `divide` | Float `0.0` as divisor | Calculator module imported | a=5.0, b=0.0 | 1. Call `divide(5.0, 0.0)` | Raises `ValueError`: "Cannot divide by zero." | Critical |

---

## Exception Handling Test Cases

| TC ID | Function | Test Scenario | Preconditions | Input Data | Test Steps | Expected Result | Priority |
|---|---|---|---|---|---|---|---|
| TC-DIV-013 | `divide` | Division by integer zero | Calculator module imported | a=5, b=0 | 1. Call `divide(5, 0)` 2. Catch exception | Raises `ValueError` with message "Cannot divide by zero." | Critical |
| TC-DIV-014 | `divide` | Division by negative zero float | Calculator module imported | a=1.0, b=-0.0 | 1. Call `divide(1.0, -0.0)` | Raises `ValueError`: "Cannot divide by zero." (−0.0 == 0 is True in Python) | Critical |
| TC-ADD-015 | `add` | Operand is a complex number | Calculator module imported | a=complex(1,2), b=3 | 1. Call `add(complex(1,2), 3)` | Raises `TypeError`: "Operand 'a' must be a number, got complex." | Low |
| TC-MUL-011 | `multiply` | Operand is a tuple | Calculator module imported | a=(1,2), b=3 | 1. Call `multiply((1,2), 3)` | Raises `TypeError`: "Operand 'a' must be a number, got tuple." | Low |
| TC-SUB-010 | `subtract` | Error message includes actual type name | Calculator module imported | a="hello", b=3 | 1. Call `subtract("hello", 3)` 2. Inspect exception message | `TypeError` message contains "str" | Medium |

---

## Coverage Analysis

| Metric | Estimated Coverage | Notes |
|---|---|---|
| Function Coverage | 100% | All 4 functions have at least one test |
| Statement Coverage | 100% | All return and raise statements triggered |
| Branch Coverage | 100% | Both True/False paths of every `if` guard covered |
| Condition Coverage | 100% | Each operand guard tested independently |
| Exception Coverage | 100% | Every `raise TypeError` and `raise ValueError` triggered |

**Total Test Cases: 40**
- Positive: 20
- Negative: 9
- Boundary: 9
- Edge Cases: 7 (includes 2 exception-class items)
- Exception Handling: 5
