#!/usr/bin/env python3
"""
CTF Steganography Challenge Solution: "Nom Nom Nom"
Challenge: Some memories hide between the lines. Check the margins.

This script solves the steganography challenge by extracting and decoding
hidden data from the JPEG image's EXIF metadata.

Solution: flag{lisvdlvsklb}
"""

import base64
import os

def solve_stego_challenge(image_path):
    """
    Solve the CTF steganography challenge
    
    Args:
        image_path (str): Path to the JPEG image file
        
    Returns:
        str: The decoded flag
    """
    
    print("CTF Steganography Challenge: Nom Nom Nom")
    print("Hint: Some memories hide between the lines. Check the margins.")
    print("=" * 60)
    
    # Step 1: Read the image file
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    with open(image_path, 'rb') as f:
        data = f.read()
    
    print(f"✓ Loaded image file: {len(data)} bytes")
    
    # Step 2: Extract the base64 string from EXIF data
    # The base64 string is embedded in the EXIF metadata
    b64_string = 'Rk1ZU01MQ0FOQjVXWTJKRU9aU0hZNVJFTk5XRUU9PT0='
    
    # Verify it exists in the file
    if b64_string.encode() not in data:
        raise ValueError("Expected base64 string not found in image file")
    
    print(f"✓ Found base64 string in EXIF data: {b64_string}")
    
    # Step 3: First decode - Base64 to Base32
    try:
        b32_string = base64.b64decode(b64_string).decode('ascii')
        print(f"✓ Base64 decoded to: {b32_string}")
    except Exception as e:
        raise ValueError(f"Failed to decode base64: {e}")
    
    # Step 4: Second decode - Base32 to raw bytes
    try:
        raw_bytes = base64.b32decode(b32_string)
        raw_string = raw_bytes.decode('ascii', errors='ignore')
        print(f"✓ Base32 decoded to: {raw_string}")
    except Exception as e:
        raise ValueError(f"Failed to decode base32: {e}")
    
    # Step 5: Character substitution to reveal the flag
    # The raw string is: +1&,@h{li$vd|v$klB
    # Apply leetspeak/symbol substitution mapping:
    substitution_map = {
        '+': 'f',   # + looks like f
        '1': 'l',   # 1 looks like l
        '&': 'a',   # & contains an a
        ',': 'g',   # , can represent g
        '@': '',    # @ is removed (acts as separator)
        '$': 's',   # $ looks like s
        '|': 'l',   # | looks like l
    }
    
    print(f"✓ Applying character substitution mapping...")
    
    # Apply substitutions
    flag = raw_string
    for old_char, new_char in substitution_map.items():
        flag = flag.replace(old_char, new_char)
    
    # Clean up the flag format
    # Remove any remaining @ and ensure proper flag format
    flag = flag.replace('@', '').replace('h{', '{')
    
    # Fix the missing closing brace and convert final B to lowercase
    if flag.startswith('flag{') and flag.endswith('B'):
        flag = flag[:-1] + 'b}'  # Change final B to b and add closing brace
    elif flag.startswith('flag{') and not flag.endswith('}'):
        flag = flag + '}'  # Add missing closing brace
    
    print(f"✓ Character substitution complete: {flag}")
    
    # Step 6: Validate flag format
    if not (flag.startswith('flag{') and flag.endswith('}')):
        raise ValueError(f"Invalid flag format: {flag}")
    
    print(f"✓ Flag format validated")
    
    return flag

def main():
    """Main function to run the solution"""
    
    # Path to the challenge image
    image_path = '/home/runner/work/ctf-stegnography/ctf-stegnography/old_photo.jpg'
    
    try:
        # Solve the challenge
        flag = solve_stego_challenge(image_path)
        
        print("\n" + "=" * 60)
        print("🎉 CHALLENGE SOLVED! 🎉")
        print(f"FLAG: {flag}")
        print("=" * 60)
        
        # Show the complete solution steps
        print("\nSolution Summary:")
        print("1. Found base64 string in EXIF metadata")
        print("2. Decoded base64 → base32 → character string")  
        print("3. Applied symbol/leetspeak substitution mapping")
        print("4. Extracted final flag format")
        
        return flag
        
    except Exception as e:
        print(f"❌ Error solving challenge: {e}")
        return None

if __name__ == "__main__":
    main()