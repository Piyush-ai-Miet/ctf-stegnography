#!/usr/bin/env python3
"""
Steganography challenge solver for "Nom Nom Nom"
Challenge: Some memories hide between the lines. Check the margins.
"""

import base64
import subprocess
import re

def get_exif_data(image_path):
    """Extract EXIF data from image"""
    try:
        result = subprocess.run(['exiftool', image_path], 
                              capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Error reading EXIF: {e}")
        return ""

def extract_user_comment(exif_data):
    """Extract User Comment from EXIF data"""
    match = re.search(r'User Comment\s*:\s*(.+)', exif_data)
    if match:
        return match.group(1).strip()
    return None

def decode_base64_base32_chain(encoded_string):
    """Decode base64 -> base32 -> result"""
    try:
        # First decode base64
        b64_decoded = base64.b64decode(encoded_string)
        b32_string = b64_decoded.decode('ascii')
        print(f"Base64 decoded: {b32_string}")
        
        # Then decode base32
        b32_decoded = base64.b32decode(b32_string)
        result = b32_decoded.decode('ascii', errors='ignore')
        print(f"Base32 decoded: {result}")
        
        return result
    except Exception as e:
        print(f"Decoding error: {e}")
        return None

def apply_nom_pattern(text, pattern_type='every_3rd'):
    """Apply the 'Nom Nom Nom' pattern hint"""
    if pattern_type == 'every_3rd':
        # Extract every 3rd character starting from different positions
        results = []
        for start in range(3):
            sequence = [text[i] for i in range(start, len(text), 3)]
            results.append(''.join(sequence))
        return results
    elif pattern_type == 'remove_symbols':
        # Remove symbols, keep alphanumeric
        return ''.join(c for c in text if c.isalnum())
    return text

def leet_speak_decode(text):
    """Decode common leet speak substitutions"""
    leet_map = {
        '1': 'i', '3': 'e', '4': 'a', '5': 's', '7': 't', '0': 'o',
        '@': 'a', '$': 's', '&': 'e', '|': 'l', '+': 't'
    }
    
    result = ''
    for c in text:
        result += leet_map.get(c, c)
    return result

def caesar_cipher(text, shift):
    """Apply Caesar cipher with given shift"""
    result = ''
    for c in text:
        if c.isalpha():
            if c.islower():
                result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c
    return result

def find_flag_format(text):
    """Look for flag format in text"""
    # Look for {something} pattern
    if '{' in text and '}' in text:
        start = text.find('{')
        end = text.find('}', start)
        if end != -1:
            return text[start:end+1]
    
    # Look for flag{something} pattern
    flag_match = re.search(r'flag\{[^}]*\}', text, re.IGNORECASE)
    if flag_match:
        return flag_match.group(0)
    
    return None

def solve_challenge():
    """Main solver function"""
    print("=== Nom Nom Nom Steganography Challenge Solver ===")
    
    # Step 1: Extract EXIF data
    print("\n1. Extracting EXIF data...")
    exif_data = get_exif_data('old_photo.jpg')
    
    user_comment = extract_user_comment(exif_data)
    if not user_comment:
        print("No User Comment found in EXIF")
        return None
    
    print(f"User Comment: {user_comment}")
    
    # Step 2: Decode the base64/base32 chain
    print("\n2. Decoding base64/base32 chain...")
    decoded_string = decode_base64_base32_chain(user_comment)
    if not decoded_string:
        return None
    
    print(f"Decoded string: {decoded_string}")
    
    # Step 3: Apply 'Nom Nom Nom' pattern (every 3rd character)
    print("\n3. Applying 'Nom Nom Nom' pattern...")
    nom_results = apply_nom_pattern(decoded_string, 'every_3rd')
    
    for i, result in enumerate(nom_results):
        print(f"Starting at position {i}, every 3rd: {result}")
        
        # Try leet speak decode
        leet_decoded = leet_speak_decode(result)
        print(f"  Leet decoded: {leet_decoded}")
        
        # Try Caesar shifts
        for shift in [1, 5, 7, 13, 25]:
            caesar_result = caesar_cipher(leet_decoded, shift)
            print(f"  Caesar shift {shift}: {caesar_result}")
            
            # Check if this looks like a flag
            if 'flag' in caesar_result.lower() or any(word in caesar_result.lower() 
                for word in ['nom', 'eat', 'food', 'yum', 'delicious', 'tasty']):
                print(f"*** POTENTIAL FLAG: {caesar_result} ***")
    
    # Step 4: Look for flag format in original decoded string
    print("\n4. Looking for flag format...")
    if '{' in decoded_string:
        flag_part = decoded_string[decoded_string.find('{'):]
        print(f"Flag part: {flag_part}")
        
        # Try leet decode on flag part
        leet_flag = leet_speak_decode(flag_part)
        print(f"Leet decoded flag part: {leet_flag}")
        
        # Try different approaches on the flag content
        if '{' in leet_flag and '}' not in leet_flag:
            flag_content = leet_flag[1:]  # Remove opening brace
            print(f"Flag content: {flag_content}")
            
            # Try Caesar shifts on flag content
            for shift in range(1, 26):
                shifted = caesar_cipher(flag_content, shift)
                if any(word in shifted.lower() for word in ['nom', 'eat', 'food', 'yum', 'delicious', 'tasty', 'hungry']):
                    potential_flag = f"flag{{{shifted.lower()}}}"
                    print(f"*** POTENTIAL FLAG: {potential_flag} ***")
    
    print("\n=== Analysis complete ===")
    return decoded_string

if __name__ == "__main__":
    solve_challenge()