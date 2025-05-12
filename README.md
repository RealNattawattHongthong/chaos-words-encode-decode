# Multi-Layer Text Encoder/Decoder

This project implements a multi-step encoding and decoding system designed to transform text through several layers of encoding, making it difficult to reverse-engineer without knowing the exact procedure.

## How It Works

The encoding process transforms plain text through multiple sequential encoding methods:

1. **Original Text → Base64**
2. **Base64 → Hex**
3. **Hex → Base64**
4. **Base64 → ROT13**
5. **ROT13 → Reverse Groups of 5**

The decoding process reverses these steps in the exact opposite order to recover the original text.

## Files in the Project

- `encode_decode.py` - Contains the main encoding and decoding functions
- `test_decode.py` - A testing script that demonstrates decoding step-by-step
- `howtosolvebyhand.txt` - Instructions for manually decoding the text
- `wordie.txt` - Sample encoded text

## Usage

```python
from encode_decode import encode, decode

# Encoding
original_text = "Your message here"
encoded = encode(original_text)
print(f"Encoded: {encoded}")

# Decoding
decoded = decode(encoded)
print(f"Decoded: {decoded}")
```

## Manual Decoding Process

To decode the text manually (as described in `howtosolvebyhand.txt`):

1. **Undo Reverse Groups of 5**
   - Split text into 5-character chunks
   - Reverse each chunk individually
   - Join them back together

2. **Undo ROT13**
   - Apply ROT13 decoding (shift letters 13 positions back)

3. **Undo First Base64**
   - Decode using Base64 to get a hex string

4. **Undo Hex Encoding**
   - Convert hex to ASCII

5. **Undo Second Base64**
   - Decode using Base64 to get original text

## Testing

Run the test decoder to see the decoding process step-by-step:

```bash
python3 test_decode.py
```