#!/usr/bin/env python3
from final_encode_decode import encode

# Test multiple encodings of the same string
original = "insta : nattawatthongthong"

# Generate multiple encodings
print("Original:", original)
for i in range(3):
    encoded = encode(original)
    print(f"\nEncoding {i+1}:\n{encoded}")
