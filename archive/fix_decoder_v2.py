#!/usr/bin/env python3
import base64
import codecs
import re

def fix_base64_padding(s):
    """Add padding to a base64 string if needed."""
    padding_needed = len(s) % 4
    if padding_needed:
        s += "=" * (4 - padding_needed)
    return s

def decode_problematic(encoded_text):
    """
    Attempt to decode the problematic encoded text step by step, with debug output
    for each layer and handling missing padding.
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
            # Marker "MARKER" was added every 10 characters
            marker_positions = []
            for i in range(10, len(layer9), 11):
                if i < len(layer9):
                    marker_positions.append(i)
            
            # Remove marker characters
            layer8 = ''.join(layer9[i] for i in range(len(layer9)) if i not in marker_positions)
            
            print(f"Layer 8 (after removing markers, first 50 chars): {layer8[:50]}...")
            print(f"Layer 8 length: {len(layer8)}")
            
            # Ensure proper padding for Base64
            layer8_padded = fix_base64_padding(layer8)
            print(f"Layer 8 with padding (length: {len(layer8_padded)}): {layer8_padded[:50]}...")
            
            # Undo Layer 8: Triple Base64 decode
            try:
                temp1 = base64.b64decode(layer8_padded)
                temp1_text = temp1.decode('utf-8')
                print(f"First Base64 decode successful: {len(temp1_text)} chars")
                print(f"Layer 7a (first 50 chars): {temp1_text[:50]}...")
                
                # Add padding if needed
                temp1_text_padded = fix_base64_padding(temp1_text)
                
                temp2 = base64.b64decode(temp1_text_padded)
                temp2_text = temp2.decode('utf-8')
                print(f"Second Base64 decode successful: {len(temp2_text)} chars")
                print(f"Layer 7b (first 50 chars): {temp2_text[:50]}...")
                
                # Add padding if needed
                temp2_text_padded = fix_base64_padding(temp2_text)
                
                temp3 = base64.b64decode(temp2_text_padded)
                layer7 = temp3.decode('utf-8')
                print(f"Third Base64 decode successful: {len(layer7)} chars")
                print(f"Layer 7 (first 50 chars): {layer7[:50]}...")
                
                # Now we are at Layer 7
                # Check if we can see signs of the interleaved pattern (X1Y2Z3)
                # in Layer 6
                print("\nAnalyzing Layer 7 for patterns...")
                
                # The encoding process:
                # Layer 6 was interleaved with X1Y2Z3
                # Layer 7 was chunks of 3 with reversal of even positions
                
                # Instead of trying to reverse these exactly, let's look for
                # patterns that might give us clues about what is in Layer 6
                
                # Look for X1Y2Z3 pattern (every other char)
                pattern_chars = re.findall(r'.(.)', layer7)
                pattern_counts = {}
                for c in pattern_chars:
                    pattern_counts[c] = pattern_counts.get(c, 0) + 1
                
                print("Character distribution in every other position:")
                for c, count in sorted(pattern_counts.items(), key=lambda x: (-x[1], x[0])):
                    print(f"'{c}': {count} occurrences")
                
                # Try different approaches for reconstructing Layer 6
                
                # Approach 1: Assume Layer 7 is approximately Layer 6 with chunks of 3,
                # where even chunks are reversed
                chunks = [layer7[i:i+3] for i in range(0, len(layer7), 3)]
                layer6_attempt1 = ''
                for i, chunk in enumerate(chunks):
                    if i % 2 == 0 and len(chunk) == 3:  # Even position, was reversed in encoding
                        layer6_attempt1 += chunk[::-1]
                    else:  # Odd position, kept as is
                        layer6_attempt1 += chunk
                
                print(f"\nLayer 6 (Approach 1, first 50 chars): {layer6_attempt1[:50]}...")
                
                # Approach 2: Assume Layer 7 is Layer 6 interleaved with X1Y2Z3
                layer6_attempt2 = ''
                for i in range(0, len(layer7), 2):
                    if i < len(layer7):
                        layer6_attempt2 += layer7[i]
                
                print(f"Layer 6 (Approach 2, first 50 chars): {layer6_attempt2[:50]}...")
                
                # Let's try both approaches
                for attempt_num, layer6 in enumerate([layer6_attempt1, layer6_attempt2], 1):
                    print(f"\n==== ATTEMPT {attempt_num} ====")
                    
                    # Assume layer6 has interleaved pattern X1Y2Z3
                    # Extract every other character
                    layer5 = ''
                    for i in range(0, len(layer6), 2):
                        if i < len(layer6):
                            layer5 += layer6[i]
                    
                    print(f"Layer 5 (after removing interleave, first 50 chars): {layer5[:50]}...")
                    
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
                        # Add padding if needed
                        layer1_padded = fix_base64_padding(layer1)
                        original_bytes = base64.b64decode(layer1_padded)
                        original = original_bytes.decode('utf-8')
                        print(f"Original decoded text: {original}")
                        
                        # If it looks like a valid result (e.g., contains "insta"), return it
                        if "insta" in original.lower():
                            print(f"Found valid result in attempt {attempt_num}!")
                            return original
                    except Exception as e:
                        print(f"Error decoding final layer in attempt {attempt_num}: {str(e)}")
                
                # If we get here, none of the attempts worked
                return "Decoding error: Could not successfully decode through all layers"
                
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

# Try with original string with fixed padding
fixed_encoded = fix_base64_padding(encoded)

print("=== ATTEMPTING TO DECODE THE PROBLEMATIC STRING ===")
print("Trying with original string (with padding fixed)...")
result = decode_problematic(fixed_encoded)
print(f"\nFinal result: {result}")

# Also try the truncated version
truncated = encoded[:-1]
truncated_fixed = fix_base64_padding(truncated)

print("\n=== TRYING WITH TRUNCATED VERSION ===")
print("Trying with truncated version (last character removed, padding fixed)...")
result_truncated = decode_problematic(truncated_fixed)
print(f"\nFinal result with truncated version: {result_truncated}")