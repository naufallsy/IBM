# Automated Test Case Generator — Methodology & Instructions

**Project:** Simple Test Generator  
**Target:** `target/calculator.py`  
**Output:** `output/generated_test_cases.md` · `output/generated_test_cases.json`  
**Unit Tests:** `tests/test_calculator.py`

---

## 1. Generator Philosophy

This generator uses **AI-driven semantic source code analysis** (via IBM Bob) rather than
purely syntactic AST traversal. The distinction matters:

| Approach | What it detects |
|---|---|
| AST parsing | Function names, parameter count, decorators |
| AI semantic analysis | Intent, invariants, business rules, implicit constraints, error semantics |

The generator combines both: it reads the source code structurally *and* reasons about
the meaning of each branch, guard clause, and return value.

---

## 2. Analysis Process

### Step 1 — Function Inventory
Read `calculator.py` and extract:
- Function name and signature (name, parameters, type hints, return type).
- Docstring (description, args, returns, raises, examples).

### Step 2 — Branch & Guard Identification
For each function, identify every conditional:
- `isinstance` guard → triggers `TypeError`.
- Value constraint guard (`b == 0`) → triggers `ValueError`.
- Normal execution path → produces a numeric result.

### Step 3 — Scenario Classification
Map each identified path to a test type:

| Path | Test Type |
|---|---|
| Valid numeric inputs, expected math result | Positive |
| Non-numeric input (str, None, list, dict) | Negative / Exception |
| Boolean input (bool is subclass of int but rejected) | Negative / Edge Case |
| Divisor = 0 | Exception |
| Large numbers, very small floats | Boundary / Edge Case |
| Negative operands, zero operands | Boundary |

### Step 4 — Test Case Generation
For each scenario, produce a structured record with all required attributes.

### Step 5 — Output Serialisation
Write the same test case data in two formats:
- Markdown table (`output/generated_test_cases.md`).
- JSON array (`output/generated_test_cases.json`).

### Step 6 — pytest Code Generation
Transform each test case record into a `pytest` test function in
`tests/test_calculator.py`.

---

## 3. Test Case Schema

Each generated test case must include:

```
test_case_id    : string   — e.g. "TC-ADD-001"
function_name   : string   — e.g. "add"
test_scenario   : string   — human-readable description
test_type       : enum     — Positive | Negative | Boundary | Edge Case | Exception
priority        : enum     — Critical | High | Medium | Low
preconditions   : string   — state before test execution
input_data      : dict     — {a: value, b: value}
test_steps      : list     — ordered steps to reproduce
expected_result : string   — what the test must assert
```

---

## 4. Naming Convention

Test Case IDs follow the pattern: `TC-{FUNC}-{SEQ}`

| Prefix | Function |
|---|---|
| `TC-ADD-xxx` | add() |
| `TC-SUB-xxx` | subtract() |
| `TC-MUL-xxx` | multiply() |
| `TC-DIV-xxx` | divide() |

Sequence numbers are zero-padded to three digits: `001`, `002`, ...

---

## 5. Priority Mapping

| Scenario Type | Default Priority |
|---|---|
| Core arithmetic correctness | Critical |
| Division by zero | Critical |
| TypeError on invalid input | High |
| Negative operands | High |
| Zero operand | High |
| Float precision | Medium |
| Large/small boundary values | Medium |
| Boolean rejection | Medium |
| None / collection input | Medium |

---

## 6. Coverage Goals

The generator targets the following coverage for `calculator.py`:

- **Function Coverage:** 100% — all four functions tested.
- **Branch Coverage:** 100% — every `if` branch (True and False) covered.
- **Condition Coverage:** 100% — each operand guard tested independently.
- **Exception Coverage:** 100% — every `raise` statement triggered at least once.

---

## 7. Limitations

- Float equality assertions use `pytest.approx()` to handle IEEE 754 precision.
- The generator does not test thread safety or performance.
- Overflow behaviour of Python's arbitrary-precision integers is not a concern here.
- The generator does not auto-regenerate on file change; re-run manually after edits.
