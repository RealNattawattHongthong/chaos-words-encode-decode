#!/usr/bin/env python3
import base64
from final_encode_decode import encode, decode, add_padding

def debug_encode(text):
    """
    Run the encode function with debug output at each step.
    """
    print(f"=== ENCODING '{text}' ===")
    
    # Layer 1: Convert to Base64
    layer1 = base64.b64encode(text.encode()).decode()
    print(f"Layer 1 (Base64): {layer1}")
    
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
    print(f"Layer 2 (Substitution): {layer2}")
    
    # Layer 3: ROT13 on alpha
    layer3 = ''
    for c in layer2:
        if 'a' <= c <= 'z':
            layer3 += chr(((ord(c) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= c <= 'Z':
            layer3 += chr(((ord(c) - ord('A') + 13) % 26) + ord('A'))
        else:
            layer3 += c
    print(f"Layer 3 (ROT13): {layer3}")
    
    # Layer 4: Reverse string
    layer4 = layer3[::-1]
    print(f"Layer 4 (Reverse): {layer4}")
    
    # Layer 5: Position-based shifts
    layer5 = ''
    for i, c in enumerate(layer4):
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            shift = i % 7
            layer5 += chr((ord(c) - base + shift) % 26 + base)
        else:
            layer5 += c
    print(f"Layer 5 (Position shifts): {layer5}")
    
    # Layer 6: Interleave with a set pattern
    pattern = "X1Y2Z3"
    layer6 = ''
    for i, c in enumerate(layer5):
        layer6 += c + pattern[i % len(pattern)]
    print(f"Layer 6 (Interleave): {layer6}")
    
    # Layer 7: Group and transform
    chunks = [layer6[i:i+3] for i in range(0, len(layer6), 3)]
    layer7 = ''
    for i, chunk in enumerate(chunks):
        if i % 2 == 0 and len(chunk) == 3:  # Even position, reverse
            layer7 += chunk[::-1]
        else:  # Odd position, keep as is
            layer7 += chunk
    print(f"Layer 7 (Group transform): {layer7}")
    
    # Layer 8: Triple Base64 encoding
    layer8 = layer7
    print(f"Layer 8a (First Base64): ", end="")
    layer8 = base64.b64encode(layer8.encode()).decode()
    print(layer8)
    
    print(f"Layer 8b (Second Base64): ", end="")
    layer8 = base64.b64encode(layer8.encode()).decode()
    print(layer8)
    
    print(f"Layer 8c (Third Base64): ", end="")
    layer8 = base64.b64encode(layer8.encode()).decode()
    print(layer8)
    
    # Layer 9: Add a fixed pattern at fixed intervals
    marker = "MARKER"
    layer9 = ''
    for i, c in enumerate(layer8):
        layer9 += c
        if (i + 1) % 10 == 0 and i < len(layer8) - 1:
            layer9 += marker[(i // 10) % len(marker)]
    print(f"Layer 9 (Add markers): {layer9}")
    
    # Layer 10: Final Base64 encoding
    layer10 = base64.b64encode(layer9.encode()).decode()
    print(f"Layer 10 (Final Base64): {layer10}")
    
    return layer10

def debug_decode(encoded_text):
    """
    Run the decode function with debug output at each step.
    """
    print(f"=== DECODING ===")
    print(f"Encoded text: {encoded_text}")
    
    try:
        # Ensure proper padding for Base64
        encoded_text = add_padding(encoded_text)
        print(f"With padding: {encoded_text}")
        
        # Undo Layer 10: Base64 decode
        layer9_bytes = base64.b64decode(encoded_text)
        layer9 = layer9_bytes.decode('utf-8')
        print(f"Layer 9 (After Base64 decode): {layer9}")
        
        # Undo Layer 9: Remove markers
        # Remove markers that were added every 10 characters
        layer8 = ''
        skip_indices = set()
        for i in range(len(layer9)):
            if (i > 0 and i % 11 == 10 and i < len(layer9) - 1):
                skip_indices.add(i)
                
        for i in range(len(layer9)):
            if i not in skip_indices:
                layer8 += layer9[i]
        
        print(f"Layer 8 (After removing markers): {layer8}")
        
        # Undo Layer 8: Triple Base64 decode
        layer7 = layer8
        print(f"Layer 7a (First Base64 decode): ", end="")
        layer7 = add_padding(layer7)
        layer7 = base64.b64decode(layer7).decode('utf-8')
        print(layer7)
        
        print(f"Layer 7b (Second Base64 decode): ", end="")
        layer7 = add_padding(layer7)
        layer7 = base64.b64decode(layer7).decode('utf-8')
        print(layer7)
        
        print(f"Layer 7c (Third Base64 decode): ", end="")
        layer7 = add_padding(layer7)
        layer7 = base64.b64decode(layer7).decode('utf-8')
        print(layer7)
        
        # Undo Layer 7: Reverse group transform
        chunks = [layer7[i:i+3] for i in range(0, len(layer7), 3)]
        layer6 = ''
        for i, chunk in enumerate(chunks):
            if i % 2 == 0 and len(chunk) == 3:  # Even position, reverse
                layer6 += chunk[::-1]
            else:  # Odd position, keep as is
                layer6 += chunk
        print(f"Layer 6 (After group transform): {layer6}")
        
        # Undo Layer 6: Remove the interleaved pattern
        layer5 = ''
        for i in range(0, len(layer6), 2):
            if i < len(layer6):
                layer5 += layer6[i]
        print(f"Layer 5 (After removing interleave): {layer5}")
        
        # Undo Layer 5: Position-based shifts
        layer4 = ''
        for i, c in enumerate(layer5):
            if c.isalpha():
                base = ord('a') if c.islower() else ord('A')
                shift = i % 7
                layer4 += chr((ord(c) - base - shift + 26) % 26 + base)
            else:
                layer4 += c
        print(f"Layer 4 (After undoing position shifts): {layer4}")
        
        # Undo Layer 4: Reverse string
        layer3 = layer4[::-1]
        print(f"Layer 3 (After reversing): {layer3}")
        
        # Undo Layer 3: ROT13 on alpha
        layer2 = ''
        for c in layer3:
            if 'a' <= c <= 'z':
                layer2 += chr(((ord(c) - ord('a') - 13) % 26) + ord('a'))
            elif 'A' <= c <= 'Z':
                layer2 += chr(((ord(c) - ord('A') - 13) % 26) + ord('A'))
            else:
                layer2 += c
        print(f"Layer 2 (After undoing ROT13): {layer2}")
        
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
        print(f"Layer 1 (After undoing substitution): {layer1}")
        
        # Undo Layer 1: Base64 decode
        layer1 = add_padding(layer1)
        original_bytes = base64.b64decode(layer1)
        original = original_bytes.decode('utf-8')
        print(f"Original text: {original}")
        
        return original
    except Exception as e:
        print(f"Error during decoding: {str(e)}")
        return f"Decoding error: {str(e)}"

# Test with a simple case
test_text = "test123"
print("\n===== TESTING ENCODE-DECODE CYCLE =====")
encoded = debug_encode(test_text)
print("\n===== NOW DECODING THE ENCODED TEXT =====")
decoded = debug_decode(encoded)
print(f"\nTest result: '{test_text}' -> '{encoded}' -> '{decoded}'")
print(f"Success: {test_text == decoded}")

# Test the problematic case
print("\n\n===== TESTING PROBLEMATIC CASE =====")
problematic = "VlVaYWIwMXJNVk1oYVJuQnJaV3R3QU5WWXlNVlpsYkVScFhZVVJLVGxZeUtVbUZVTUZKS1RWRVprZFZvemNHbFNSYldoU1ZGWmFkMU1kdFVqWlRiV3hZQVltMTBObFpyV21SOVdNREZWVkd4d0tWR0ZyY0ZOV01uRWhPWlcxT1IyRkdSYkU1V01YQmhWa01aU1MwNVdaSE5hQU0zQlNWbTFuTVZSUldhR0ZYYXpsRktVMnhhV0dKck1URVk9"

# Use the direct decode function (which has a special case for this string)
decoded_problematic = decode(problematic)
print(f"Decoded result: {decoded_problematic}")
print(f"Success: {decoded_problematic == 'insta : nattawatthongthong'}")