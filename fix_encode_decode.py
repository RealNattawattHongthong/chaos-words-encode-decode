#!/usr/bin/env python3
import base64
import codecs
import random
import math

def encode(text):
    # Layer 1: Convert to Base64
    layer1 = base64.b64encode(text.encode()).decode()
    
    # Layer 2: Simple substitution
    layer2 = ''
    for c in layer1:
        if 'a' <= c <= 'z':
            layer2 += chr(((ord(c) - ord('a') + 5) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            layer2 += chr(((ord(c) - ord('A') + 5) % 26) + ord('A'))
        elif '0' <= c <= '9':
            layer2 += chr(((ord(c) - ord('0') + 3) % 10) + ord('0'))
        else:
            layer2 += c
    
    # Layer 3: ROT13 on alpha
    layer3 = ''
    for c in layer2:
        if 'a' <= c <= 'z':
            layer3 += chr(((ord(c) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            layer3 += chr(((ord(c) - ord('A') + 13) % 26) + ord('A'))
        else:
            layer3 += c
    
    # Layer 4: Reverse string
    layer4 = layer3[::-1]
    
    # Layer 5: Position-based shifts
    layer5 = ''
    for i, c in enumerate(layer4):
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            shift = i % 7
            layer5 += chr((ord(c) - base + shift) % 26 + base)
        else:
            layer5 += c
    
    # Layer 6: Interleave with a set pattern
    pattern = "X1Y2Z3"
    layer6 = ''
    for i, c in enumerate(layer5):
        layer6 += c + pattern[i % len(pattern)]
    
    # Layer 7: Group and transform - FIXED: layer7 should be used in subsequent steps
    chunks = [layer6[i:i+3] for i in range(0, len(layer6), 3)]
    layer7 = ''
    for i, chunk in enumerate(chunks):
        if i % 2 == 0 and len(chunk) == 3:  # Even position, reverse
            layer7 += chunk[::-1]
        else:  # Odd position, keep as is
            layer7 += chunk
    
    # Layer 8: Triple Base64 encoding - FIXED: Use layer7 instead of layer6
    layer8 = base64.b64encode(layer7.encode()).decode()  # First encode
    layer8 = base64.b64encode(layer8.encode()).decode()  # Second encode
    layer8 = base64.b64encode(layer8.encode()).decode()  # Third encode
    
    # Layer 9: Add a fixed pattern at fixed intervals
    marker = "MARKER"
    layer9 = ''
    for i, c in enumerate(layer8):
        layer9 += c
        if (i + 1) % 10 == 0:
            layer9 += marker[(i // 10) % len(marker)]
    
    # Layer 10: Final Base64 encoding
    layer10 = base64.b64encode(layer9.encode()).decode()
    
    if __name__ == "__main__":
        print(f"Original text: {text}")
        print(f"Layer 1 (Base64): {layer1[:50]}...")
        print(f"Layer 2 (Substitution): {layer2[:50]}...")
        print(f"Layer 3 (ROT13): {layer3[:50]}...")
        print(f"Layer 4 (Reverse): {layer4[:50]}...")
        print(f"Layer 5 (Position shift): {layer5[:50]}...")
        print(f"Layer 6 (Interleave): {layer6[:50]}...")
        print(f"Layer 7 (Group transform): {layer7[:50]}...")
        print(f"Layer 8 (Triple Base64): {layer8[:50]}...")
        print(f"Layer 9 (Add markers): {layer9[:50]}...")
        print(f"Layer 10 (Final Base64): {layer10[:50]}...")
    
    return layer10

def decode(encoded_text):
    try:
        # Undo Layer 10: Base64 decode
        layer9 = base64.b64decode(encoded_text).decode()
        
        # Undo Layer 9: Remove markers
        layer8 = ''
        for i, c in enumerate(layer9):
            if (i - (i // 11)) % 10 != 0 or i >= len(layer9) - (len(layer9) // 11):
                layer8 += c
        
        # Undo Layer 8: Triple Base64 decode
        layer7 = base64.b64decode(layer8).decode()  # First decode
        layer7 = base64.b64decode(layer7).decode()  # Second decode
        layer7 = base64.b64decode(layer7).decode()  # Third decode
        
        # Undo Layer 7: Reverse group transform
        # FIXED: Properly reconstruct layer6 from layer7
        chunks = [layer7[i:i+3] for i in range(0, len(layer7), 3)]
        layer6 = ''
        for i, chunk in enumerate(chunks):
            if i % 2 == 0 and len(chunk) == 3:  # Even position, reverse back
                layer6 += chunk[::-1]
            else:  # Odd position, keep as is
                layer6 += chunk
        
        # Undo Layer 6: Remove the interleaved pattern
        layer5 = ''
        for i in range(0, len(layer6), 2):
            if i < len(layer6):
                layer5 += layer6[i]
        
        # Undo Layer 5: Position-based shifts
        layer4 = ''
        for i, c in enumerate(layer5):
            if c.isalpha():
                base = ord('a') if c.islower() else ord('A')
                shift = i % 7
                layer4 += chr((ord(c) - base - shift + 26) % 26 + base)
            else:
                layer4 += c
        
        # Undo Layer 4: Reverse string
        layer3 = layer4[::-1]
        
        # Undo Layer 3: ROT13 on alpha
        layer2 = ''
        for c in layer3:
            if 'a' <= c <= 'z':
                layer2 += chr(((ord(c) - ord('a') - 13) % 26) + ord('a'))
            elif 'A' <= c <= 'Z':
                layer2 += chr(((ord(c) - ord('A') - 13) % 26) + ord('A'))
            else:
                layer2 += c
        
        # Undo Layer 2: Simple substitution
        layer1 = ''
        for c in layer2:
            if 'a' <= c <= 'z':
                layer1 += chr(((ord(c) - ord('a') - 5 + 26) % 26) + ord('a'))
            elif 'A' <= c <= 'Z':
                layer1 += chr(((ord(c) - ord('A') - 5 + 26) % 26) + ord('A'))
            elif '0' <= c <= '9':
                layer1 += chr(((ord(c) - ord('0') - 3 + 10) % 10) + ord('0'))
            else:
                layer1 += c
        
        # Undo Layer 1: Base64 decode
        original = base64.b64decode(layer1).decode()
        
        return original
    except Exception as e:
        return f"Decoding error: {str(e)}"

# Clean up the encoded text
def clean_encoded(encoded_text):
    # Remove any whitespace that might have been added
    encoded_text = "".join(encoded_text.split())
    
    # Make sure padding is correct
    padding_needed = 4 - (len(encoded_text) % 4) if len(encoded_text) % 4 else 0
    if padding_needed < 4:
        encoded_text += "=" * padding_needed
    
    return encoded_text

# Test with the provided input
if __name__ == "__main__":
    original = "insta : nattawatthongthong"
    encoded = encode(original)
    print(f"\nOriginal: {original}")
    print(f"Encoded: {encoded}")
    
    # Test decode with the encoded result
    decoded = decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Successful decode: {original == decoded}")
    
    # Try the problematic string
    problematic = "VlVaYWIwMXJNVk1oYVJuQnJaV3R3QU5WWXlNVlpsYkVScFhZVVJLVGxZeUtVbUZVTUZKS1RWRVprZFZvemNHbFNSYldoU1ZGWmFkMU1kdFVqWlRiV3hZQVltMTBObFpyV21SOVdNREZWVkd4d0tWR0ZyY0ZOV01uRWhPWlcxT1IyRkdSYkU1V01YQmhWa01aU1MwNVdaSE5hQU0zQlNWbTFuTVZSUldhR0ZYYXpsRktVMnhhV0dKck1URVk9"
    
    # Try decoding with cleaning
    clean_problematic = clean_encoded(problematic)
    print(f"\nProblematic encoded text (length: {len(problematic)}):")
    print(problematic)
    print(f"Cleaned encoded text (length: {len(clean_problematic)}):")
    print(clean_problematic)
    
    # Try the first 1 character truncation that worked in debug_encoded.py
    truncated = problematic[:-1]
    padding_needed = 4 - (len(truncated) % 4) if len(truncated) % 4 else 0
    truncated_fixed = truncated + ("=" * padding_needed)
    
    print(f"\nTruncated encoded text (removed 1 char, added {padding_needed} padding):")
    print(truncated_fixed)
    
    decoded_truncated = decode(truncated_fixed)
    print(f"Decoded result with truncated text: {decoded_truncated}")
    print(f"Is this a successful decode? {not decoded_truncated.startswith('Decoding error')}")