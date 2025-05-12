#!/usr/bin/env python3
import base64

# The problematic encoded string
encoded = "VlVaYWIwMXJNVk1oYVJuQnJaV3R3QU5WWXlNVlpsYkVScFhZVVJLVGxZeUtVbUZVTUZKS1RWRVprZFZvemNHbFNSYldoU1ZGWmFkMU1kdFVqWlRiV3hZQVltMTBObFpyV21SOVdNREZWVkd4d0tWR0ZyY0ZOV01uRWhPWlcxT1IyRkdSYkU1V01YQmhWa01aU1MwNVdaSE5hQU0zQlNWbTFuTVZSUldhR0ZYYXpsRktVMnhhV0dKck1URVk9"

# Try to decode layer by layer
try:
    # Try layer 10 decode
    print("=== DETAILED ANALYSIS OF ENCODED STRING ===")
    print(f"Length of encoded string: {len(encoded)}")
    print(f"Characters in encoded string: {encoded}")
    
    # Check for invalid characters
    print("\nChecking for invalid Base64 characters...")
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
    invalid_chars = [c for c in encoded if c not in valid_chars]
    if invalid_chars:
        print(f"Found invalid characters: {invalid_chars}")
    else:
        print("All characters are valid Base64 characters")
    
    # Try different padding approaches
    print("\nTrying different padding approaches:")
    
    # No padding
    print("\n1. Original string (no modifications):")
    try:
        decoded = base64.b64decode(encoded)
        print(f"Successfully decoded! Length: {len(decoded)}")
    except Exception as e:
        print(f"Failed: {str(e)}")
    
    # Add padding
    print("\n2. With padding added:")
    padding_needed = 4 - (len(encoded) % 4) if len(encoded) % 4 else 0
    padded = encoded + ("=" * padding_needed)
    try:
        decoded = base64.b64decode(padded)
        print(f"Successfully decoded with {padding_needed} padding chars! Length: {len(decoded)}")
    except Exception as e:
        print(f"Failed: {str(e)}")
    
    # Try removing characters
    for i in range(1, 4):
        print(f"\n3.{i} Removing {i} character(s) from the end:")
        truncated = encoded[:-i]
        padding_needed = 4 - (len(truncated) % 4) if len(truncated) % 4 else 0
        padded_truncated = truncated + ("=" * padding_needed)
        try:
            decoded = base64.b64decode(padded_truncated)
            print(f"Successfully decoded after removing {i} char(s) and adding {padding_needed} padding! Length: {len(decoded)}")
            # Try to decode as text
            try:
                text = decoded.decode('utf-8')
                print(f"First 50 chars of decoded text: {text[:50]}...")
                print("This could be layer 9 in the decoding process")
            except UnicodeDecodeError:
                print("Decoded bytes could not be converted to UTF-8 text")
        except Exception as e:
            print(f"Failed: {str(e)}")
    
    print("\n=== ANALYSIS COMPLETE ===")
    
except Exception as e:
    print(f"Error during analysis: {str(e)}")