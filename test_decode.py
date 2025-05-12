#!/usr/bin/env python3
import base64
import codecs
from encode_decode import decode

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
        for i, c in enumerate(layer9):
            if (i - (i // 11)) % 10 != 0 or i >= len(layer9) - (len(layer9) // 11):
                layer8 += c
        print("\nStep 2 (After removing markers):\n", layer8[:100], "..." if len(layer8) > 100 else "")
        
        # Step 3: Undo Layer 8: Triple Base64 decode
        layer7 = base64.b64decode(layer8).decode()  # First decode
        print("\nStep 3a (After first Base64 decode):\n", layer7[:100], "..." if len(layer7) > 100 else "")
        
        layer6_1 = base64.b64decode(layer7).decode()  # Second decode
        print("\nStep 3b (After second Base64 decode):\n", layer6_1[:100], "..." if len(layer6_1) > 100 else "")
        
        layer6 = base64.b64decode(layer6_1).decode()  # Third decode
        print("\nStep 3c (After third Base64 decode):\n", layer6[:100], "..." if len(layer6) > 100 else "")
        
        # Step 4: Undo Layer 7: Reverse group transform
        layer6_reconstructed = layer6  # We'll use the original layer6 from triple Base64
        print("\nStep 4 (Layer 7 reconstruction):\n", "Using the original Layer 6 from triple Base64 decode")
        
        # Step 5: Undo Layer 6: Remove the interleaved pattern
        layer5 = ''
        for i in range(0, len(layer6_reconstructed), 2):
            if i < len(layer6_reconstructed):
                layer5 += layer6_reconstructed[i]
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
        original = base64.b64decode(layer1).decode()
        print("\nStep 10 (Final decoded result):\n", original)
        
        # Verify with the full decode function
        print("\n=== VERIFICATION ===")
        full_decode = decode(encoded_text)
        print("Full decode result (using decode function):\n", full_decode)
        print(f"Match with step-by-step: {full_decode == original}")
        
        print("\n=== DECODING COMPLETE ===")
        
    except Exception as e:
        print(f"\nError during decoding at step: {str(e)}")
        print("Try the full decode function to see if it can handle this error.")
        
        try:
            full_decode = decode(encoded_text)
            print("\nFull decode result (using decode function):\n", full_decode)
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
            from encode_decode import encode
            original = "This is a test of the 10-layer encoder and decoder system"
            encoded_text = encode(original)
            print(f"Generated new encoded text from: '{original}'")
            step_by_step_decode(encoded_text)
            
    except FileNotFoundError:
        # Generate a fresh example if file not found
        from encode_decode import encode
        original = "This is a test of the 10-layer encoder and decoder system"
        encoded_text = encode(original)
        print(f"Generated new encoded text from: '{original}'")
        step_by_step_decode(encoded_text)