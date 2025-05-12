#!/usr/bin/env python3
import base64
import codecs

def decode_problematic(encoded_text):
    """
    Attempt to decode the problematic encoded text step by step, with debug output
    for each layer.
    """
    print(f"Starting with encoded text (length: {len(encoded_text)})")
    
    try:
        # Try the base64 decode directly
        first_decode = base64.b64decode(encoded_text)
        print(f"Layer 10 decoded successfully: {len(first_decode)} bytes")
        
        # Try to convert to text
        try:
            layer9 = first_decode.decode('utf-8')
            print(f"Layer 9 (as text, first 50 chars): {layer9[:50]}...")
            
            # Analyze the content
            print(f"Layer 9 length: {len(layer9)}")
            
            # Undo Layer 9: Remove markers
            # In the original code, marker was added every 10 characters
            marker = "MARKER"
            marker_positions = []
            
            # Print characters at positions that are multiples of 10
            for i in range(10, len(layer9), 11):
                if i < len(layer9):
                    print(f"Char at position {i}: '{layer9[i]}'")
                    marker_positions.append(i)
            
            # Reconstructing layer8 by removing the marker characters
            layer8 = ''
            for i in range(len(layer9)):
                if i not in marker_positions:
                    layer8 += layer9[i]
            
            print(f"Layer 8 (after removing markers, first 50 chars): {layer8[:50]}...")
            print(f"Layer 8 length: {len(layer8)}")
            
            # Undo Layer 8: Triple Base64 decode
            try:
                temp1 = base64.b64decode(layer8)
                print(f"First Base64 decode successful: {len(temp1)} bytes")
                
                temp1_text = temp1.decode('utf-8')
                print(f"Layer 7a (first Base64 decode, first 50 chars): {temp1_text[:50]}...")
                
                temp2 = base64.b64decode(temp1_text)
                print(f"Second Base64 decode successful: {len(temp2)} bytes")
                
                temp2_text = temp2.decode('utf-8')
                print(f"Layer 7b (second Base64 decode, first 50 chars): {temp2_text[:50]}...")
                
                temp3 = base64.b64decode(temp2_text)
                print(f"Third Base64 decode successful: {len(temp3)} bytes")
                
                layer7 = temp3.decode('utf-8')
                print(f"Layer 7 (third Base64 decode, first 50 chars): {layer7[:50]}...")
                print(f"Layer 7 length: {len(layer7)}")
                
                # Analyze layer7 characters for pattern
                print("Analyzing layer7 characters:")
                for i in range(min(30, len(layer7))):
                    print(f"Position {i}: '{layer7[i]}'")
                
                # Layer 7 was created by grouping layer6 into chunks of 3
                # and reversing the chunks at even positions
                # We need to reconstruct layer6 from layer7
                
                chunks = [layer7[i:i+3] for i in range(0, len(layer7), 3)]
                layer6 = ''
                for i, chunk in enumerate(chunks):
                    if i % 2 == 0 and len(chunk) == 3:  # Even position, was reversed in encoding
                        layer6 += chunk[::-1]
                    else:  # Odd position, kept as is
                        layer6 += chunk
                
                print(f"Layer 6 (after chunk transform, first 50 chars): {layer6[:50]}...")
                print(f"Layer 6 length: {len(layer6)}")
                
                # Analyze layer6 characters for pattern
                print("\nAnalyzing layer6 characters and checking for X1Y2Z3 pattern:")
                for i in range(min(30, len(layer6))):
                    print(f"Position {i}: '{layer6[i]}'")
                
                # Layer 6 was created by interleaving with pattern X1Y2Z3
                # We need to remove the pattern
                pattern = "X1Y2Z3"
                layer5 = ''
                for i in range(0, len(layer6), 2):
                    if i < len(layer6):
                        char = layer6[i]
                        layer5 += char
                        # Check if next char matches expected pattern
                        if i+1 < len(layer6):
                            expected_pattern = pattern[(i//2) % len(pattern)]
                            actual = layer6[i+1]
                            if actual != expected_pattern:
                                print(f"Warning: At position {i+1}, expected '{expected_pattern}' but got '{actual}'")
                
                print(f"Layer 5 (after removing interleave, first 50 chars): {layer5[:50]}...")
                print(f"Layer 5 length: {len(layer5)}")
                
                # Continue with the rest of the decoding...
                # Layer 5: Position-based shifts
                layer4 = ''
                for i, c in enumerate(layer5):
                    if c.isalpha():
                        base = ord('a') if c.islower() else ord('A')
                        shift = i % 7
                        layer4 += chr((ord(c) - base - shift + 26) % 26 + base)
                    else:
                        layer4 += c
                
                print(f"Layer 4 (after undoing position shifts, first 50 chars): {layer4[:50]}...")
                
                # Layer 4: Reverse string
                layer3 = layer4[::-1]
                print(f"Layer 3 (after reversing, first 50 chars): {layer3[:50]}...")
                
                # Layer 3: ROT13 on alpha
                layer2 = ''
                for c in layer3:
                    if 'a' <= c <= 'z':
                        layer2 += chr(((ord(c) - ord('a') - 13) % 26) + ord('a'))
                    elif 'A' <= c <= 'Z':
                        layer2 += chr(((ord(c) - ord('A') - 13) % 26) + ord('A'))
                    else:
                        layer2 += c
                
                print(f"Layer 2 (after ROT13 decode, first 50 chars): {layer2[:50]}...")
                
                # Layer 2: Simple substitution
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
                
                print(f"Layer 1 (after substitution decode, first 50 chars): {layer1[:50]}...")
                
                # Layer 1: Base64 decode
                try:
                    original_bytes = base64.b64decode(layer1)
                    original = original_bytes.decode('utf-8')
                    print(f"Original decoded text: {original}")
                    return original
                except Exception as e:
                    print(f"Error decoding final layer: {str(e)}")
                    return f"Decoding error in final layer: {str(e)}"
                
            except Exception as e:
                print(f"Error during triple Base64 decode: {str(e)}")
                return f"Decoding error during triple Base64 decode: {str(e)}"
            
        except UnicodeDecodeError:
            print("First decode result could not be converted to text")
            return "Decoding error: First decode result is not valid UTF-8 text"
        
    except Exception as e:
        print(f"Initial Base64 decode failed: {str(e)}")
        return f"Decoding error: {str(e)}"

# The problematic encoded string
encoded = "VlVaYWIwMXJNVk1oYVJuQnJaV3R3QU5WWXlNVlpsYkVScFhZVVJLVGxZeUtVbUZVTUZKS1RWRVprZFZvemNHbFNSYldoU1ZGWmFkMU1kdFVqWlRiV3hZQVltMTBObFpyV21SOVdNREZWVkd4d0tWR0ZyY0ZOV01uRWhPWlcxT1IyRkdSYkU1V01YQmhWa01aU1MwNVdaSE5hQU0zQlNWbTFuTVZSUldhR0ZYYXpsRktVMnhhV0dKck1URVk9"

# Try the first 1 character truncation that worked in debug_encoded.py
truncated = encoded[:-1]
padding_needed = 4 - (len(truncated) % 4) if len(truncated) % 4 else 0
truncated_fixed = truncated + ("=" * padding_needed)

print("=== ATTEMPTING TO DECODE THE PROBLEMATIC STRING ===")
print("Trying with truncated version (last character removed)...")
result = decode_problematic(truncated_fixed)
print(f"\nFinal result: {result}")

# If the above fails, try modifying additional code in decode function