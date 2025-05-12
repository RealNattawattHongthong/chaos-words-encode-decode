#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.encoder_decoder import encode, decode

# Generate a new encoded string
original = "hello world"
print(f"Original: {original}")

# Encode using the 10-layer encoder
encoded = encode(original)
print(f"Encoded: {encoded}")

# Decode using our new decoder
print("\n=== Decoding with new decoder ===")
decoded = decode(encoded)

# Verify
print(f"\nVerification: Original '{original}' == Decoded '{decoded}': {original == decoded}")