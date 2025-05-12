#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.core.encoder_decoder import decode

# The two keys provided by the user
key1 = "VlVaYWIwMXJNVk1oYVJuQnJaV3R3QU5WWXlNVlpsYkVScFhZVVJLVGxZeUtVbUZVTUZKS1RWRVprZFZvemNHbFNSYldoU1ZGWmFkMU1kdFVqWlRiV3hZQVltMTBObFpyV21SOVdNREZWVkd4d0tWR0ZyY0ZOV01uRWhPWlcxT1IyRkdSYkU1V01YQmhWa01aU1MwNVdaSE5hQU0zQlNWbTFuTVZSUldhR0ZYYXpsRktVMnhhV0dKck1URVk9"
key2 = "V2tkNGJrOVZNVk1oYVJuQnFZV3R2QWVsWXlNVlpsYlZSSnpZVVZhVGxZeUtVbUZVYkZKS1RrRVprZFZvemNGWlNSYldoNlZGWmFkMU1kc2JIRlRhazVZQVltMTBObFp0ZUdSOVdWVEZWVkd4d0tWbFpGY0V4V01uRWhPWld4a1IyRklSWkU1V01YQmhXbE1aU1MxUnNaSE5hQU0zQnNWbTFvUTFSUldhR0ZYYkZwVktVMVJTV0dKck1URVk9"

# Decode both keys
print("First key decodes to:", decode(key1))
print("Second key decodes to:", decode(key2))