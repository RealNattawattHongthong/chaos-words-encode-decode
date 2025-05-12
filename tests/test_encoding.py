#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.encoder_decoder import encode

# Test multiple encodings of the same string
original = "insta : nattawatthongthong"

# Generate multiple encodings
print("Original:", original)
for i in range(3):
    encoded = encode(original)
    print(f"\nEncoding {i+1}:\n{encoded}")
