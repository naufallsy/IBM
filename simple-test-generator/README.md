# Simple Test Generator

AI-Powered Automated Test Case Generator — targeting a Simple Calculator written in Python 3.

## Project Structure

```
simple-test-generator/
│
├── target/
│   └── calculator.py          # Target application under test
│
├── generator/
│   └── test_case_generator.md # Generator instructions & methodology
│
├── output/
│   ├── generated_test_cases.md   # Test cases in Markdown table format
│   └── generated_test_cases.json # Test cases in JSON format
│
├── tests/
│   └── test_calculator.py     # pytest unit tests (auto-generated)
│
└── README.md                  # This file
```

## Quick Start

### 1. Install dependencies

```bash
pip install pytest
```

### 2. Run the generated unit tests

```bash
cd simple-test-generator
pytest tests/test_calculator.py -v
```

### 3. View generated test cases

- Markdown: `output/generated_test_cases.md`
- JSON:      `output/generated_test_cases.json`

## Calculator Functions

| Function | Signature | Description |
|---|---|---|
| `add` | `add(a, b) -> float` | Returns a + b |
| `subtract` | `subtract(a, b) -> float` | Returns a - b |
| `multiply` | `multiply(a, b) -> float` | Returns a * b |
| `divide` | `divide(a, b) -> float` | Returns a / b; raises ValueError if b == 0 |

## Error Handling

- `TypeError`  — raised when either operand is not a numeric type (int/float), including booleans.
- `ValueError` — raised by `divide()` when the divisor is zero.

## Notes

- The generator (`generator/`) is completely separate from the target application (`target/`).
- Do **not** import generator code into the target application.
- Test files in `tests/` are generated outputs — do not edit them manually unless regenerating.
