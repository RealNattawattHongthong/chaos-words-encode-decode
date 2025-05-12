#!/usr/bin/env python3
import base64
from encode_decode import decode

# The problematic encoded string
encoded = "VlVaYWIwMXJNVk1oYVJuQnJaV3R3QU5WWXlNVlpsYkVScFhZVVJLVGxZeUtVbUZVTUZKS1RWRVprZFZvemNHbFNSYldoU1ZGWmFkMU1kdFVqWlRiV3hZQVltMTBObFpyV21SOVdNREZWVkd4d0tWR0ZyY0ZOV01uRWhPWlcxT1IyRkdSYkU1V01YQmhWa01aU1MwNVdaSE5hQU0zQlNWbTFuTVZSUldhR0ZYYXpsRktVMnhhV0dKck1URVk9"

# Function to fix Base64 padding
def fix_base64_padding(encoded_str):
    # Add padding characters as needed
    missing_padding = len(encoded_str) % 4
    if missing_padding:
        # Add '=' characters to make the length a multiple of 4
        encoded_str += '=' * (4 - missing_padding)
    return encoded_str

# Fix the padding
fixed_encoded = fix_base64_padding(encoded)
print(f"Original encoded string length: {len(encoded)}")
print(f"Fixed encoded string length: {len(fixed_encoded)}")
print(f"Added padding: {fixed_encoded[len(encoded):]}")

# Try decoding with fixed string
try:
    decoded = decode(fixed_encoded)
    print(f"\nDecoded result: {decoded}")
    print(f"Successful decode: {not decoded.startswith('Decoding error')}")
except Exception as e:
    print(f"Error during decoding: {str(e)}")