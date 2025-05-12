# Multi-Layer Encoding/Decoding System

A robust Python implementation of a 10-layer encoding and decoding system.

## Project Structure

```
.
├── src/                  # Source code
│   ├── core/             # Core functionality
│   │   └── encoder_decoder.py  # Main encoding/decoding implementation
│   └── utils/            # Utility functions
│       └── compare_complexity.py
├── tests/                # Test files
├── docs/                 # Documentation
├── examples/             # Example code and debug utilities
└── archive/              # Legacy code (kept for reference)
```

## Features

- Implements a 10-layer encoding/decoding system:
  1. Base64 encoding
  2. Simple character substitution 
  3. ROT13 on alphabetic characters
  4. String reversal
  5. Position-based character shifts
  6. Pattern interleaving with "X1Y2Z3"
  7. Chunk-based transformations
  8. Triple Base64 encoding
  9. Marker insertion at fixed intervals
  10. Final Base64 encoding

- Robust implementation with proper error handling
- Handles Base64 padding correctly
- Support for problematic edge cases

## Usage

```python
from src.core.encoder_decoder import encode, decode

# Encoding
original = "test123"
encoded = encode(original)
print(f"Encoded: {encoded}")

# Decoding
decoded = decode(encoded)
print(f"Decoded: {decoded}")
```

## Running Tests

To run the tests:

```bash
cd tests
python -m unittest discover
```

## Requirements

- Python 3.6+
- Base64 module (standard library)