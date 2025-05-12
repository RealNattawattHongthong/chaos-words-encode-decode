#!/usr/bin/env python3
from final_encode_decode import encode
from decode import decode

# Generate a new encoded string
original = "hello world"
print(f"Original: {original}")

# Encode using the 10-layer encoder
encoded = encode(original)
print(f"Encoded: {encoded}")

# Decode using our new decoder with debug output
print("\n=== Decoding with new decoder (debug mode) ===")
decoded = decode(encoded, debug=True)

# Verify
print(f"\nVerification: Original '{original}' == Decoded '{decoded}': {original == decoded}")