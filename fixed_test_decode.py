#!/usr/bin/env python3
import base64
import codecs

def add_padding(s):
    """Add proper padding to a base64 string."""
    padding_needed = len(s) % 4
    if padding_needed:
        s += "=" * (4 - padding_needed)
    return s

def step_by_step_decode(encoded_text):
    try:
        print("\n=== MULTI-LAYER DECODER (10 Layers) ===\n")
        print(f"Encoded text:\n{encoded_text}\n")
        print("Starting decoding process...\n")
        
        # Step 1: Undo Layer 10: Base64 decode
        layer9 = base64.b64decode(encoded_text).decode()
        print("Step 1 (After undoing Base64):\n", layer9[:100], "..." if len(layer9) > 100 else "")
        
        # Step 2: Undo Layer 9: Remove markers
        layer8 = ''
        skip_indices = set()
        for i in range(len(layer9)):
            if (i > 0 and i % 11 == 10 and i < len(layer9) - 1):
                skip_indices.add(i)
                
        for i in range(len(layer9)):
            if i not in skip_indices:
                layer8 += layer9[i]
        print("\nStep 2 (After removing markers):\n", layer8[:100], "..." if len(layer8) > 100 else "")
        
        # Step 3: Undo Layer 8: Triple Base64 decode
        layer7 = layer8
        for j in range(3):  # Triple decode
            layer7 = add_padding(layer7)  # Ensure proper padding
            layer7 = base64.b64decode(layer7).decode()
            print(f"\nStep 3{chr(97+j)} (After Base64 decode #{j+1}):\n", layer7[:100], "..." if len(layer7) > 100 else "")
        
        # Step 4: Undo Layer 7: Reverse group transform
        chunks = [layer7[i:i+3] for i in range(0, len(layer7), 3)]
        layer6 = ''
        for i, chunk in enumerate(chunks):
            if i % 2 == 0 and len(chunk) == 3:  # Even position, reverse
                layer6 += chunk[::-1]
            else:  # Odd position, keep as is
                layer6 += chunk
        print("\nStep 4 (After undoing group transform):\n", layer6[:100], "..." if len(layer6) > 100 else "")
        
        # Step 5: Undo Layer 6: Remove the interleaved pattern
        layer5 = ''
        for i in range(0, len(layer6), 2):
            if i < len(layer6):
                layer5 += layer6[i]
        print("\nStep 5 (After removing interleaved pattern):\n", layer5[:100], "..." if len(layer5) > 100 else "")
        
        # Step 6: Undo Layer 5: Position-based shifts
        layer4 = ''
        for i, c in enumerate(layer5):
            if c.isalpha():
                base = ord('a') if c.islower() else ord('A')
                shift = i % 7
                layer4 += chr((ord(c) - base - shift + 26) % 26 + base)
            else:
                layer4 += c
        print("\nStep 6 (After undoing position shifts):\n", layer4[:100], "..." if len(layer4) > 100 else "")
        
        # Step 7: Undo Layer 4: Reverse string
        layer3 = layer4[::-1]
        print("\nStep 7 (After undoing reverse):\n", layer3[:100], "..." if len(layer3) > 100 else "")
        
        # Step 8: Undo Layer 3: ROT13 on alpha
        layer2 = ''
        for c in layer3:
            if 'a' <= c <= 'z':
                layer2 += chr(((ord(c) - ord('a') - 13) % 26) + ord('a'))
            elif 'A' <= c <= 'Z':
                layer2 += chr(((ord(c) - ord('A') - 13) % 26) + ord('A'))
            else:
                layer2 += c
        print("\nStep 8 (After undoing ROT13):\n", layer2[:100], "..." if len(layer2) > 100 else "")
        
        # Step 9: Undo Layer 2: Simple substitution
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
        print("\nStep 9 (After undoing substitution):\n", layer1[:100], "..." if len(layer1) > 100 else "")
        
        # Step 10: Undo Layer 1: Base64 decode
        layer1 = add_padding(layer1)  # Ensure proper padding
        original = base64.b64decode(layer1).decode()
        print("\nStep 10 (Final decoded result):\n", original)
        
        # Verify with the full decode function from final_encode_decode
        print("\n=== VERIFICATION ===")
        from final_encode_decode import decode
        full_decode = decode(encoded_text)
        print("Full decode result (using fixed decode function):\n", full_decode)
        print(f"Match with step-by-step: {full_decode == original}")
        
        print("\n=== DECODING COMPLETE ===")
        
    except Exception as e:
        print(f"\nError during decoding at step: {str(e)}")
        print("Try the full decode function to see if it can handle this error.")
        
        try:
            from final_encode_decode import decode
            full_decode = decode(encoded_text)
            print("\nFull decode result (using fixed decode function):\n", full_decode)
        except Exception as e2:
            print(f"Full decode also failed: {str(e2)}")

if __name__ == "__main__":
    try:
        # Try to read from wordie.txt
        with open('wordie.txt', 'r') as file:
            lines = file.readlines()
            encoded_text = None
            for line in lines:
                if line.strip().startswith('Encoded:'):
                    encoded_text = line.split(':', 1)[1].strip()
                    break
        
        # If found in file, use that
        if encoded_text:
            print(f"Found encoded text in wordie.txt")
            step_by_step_decode(encoded_text)
        else:
            # Otherwise generate a fresh example
            from final_encode_decode import encode
            original = "This is a test of the 10-layer encoder and decoder system"
            encoded_text = encode(original)
            print(f"Generated new encoded text from: '{original}'")
            step_by_step_decode(encoded_text)
            
    except FileNotFoundError:
        # Generate a fresh example if file not found
        from final_encode_decode import encode
        original = "This is a test of the 10-layer encoder and decoder system"
        encoded_text = encode(original)
        print(f"Generated new encoded text from: '{original}'")
        step_by_step_decode(encoded_text)