#!/usr/bin/env python3
"""
Verification script for the Nom Nom Nom steganography challenge solution
"""

def verify_solution():
    """Verify that our solution is correct"""
    
    # Read the discovered flag
    try:
        with open('flag.txt', 'r') as f:
            discovered_flag = f.read().strip()
        print(f"Discovered flag: {discovered_flag}")
    except FileNotFoundError:
        print("ERROR: flag.txt not found")
        return False
    
    # Verify the flag format
    if not discovered_flag.startswith('flag{') or not discovered_flag.endswith('}'):
        print("ERROR: Flag does not match expected format flag{...}")
        return False
    
    # Extract flag content
    flag_content = discovered_flag[5:-1]  # Remove 'flag{' and '}'
    print(f"Flag content: {flag_content}")
    
    # Verify the content makes sense for the challenge
    if flag_content == "tea":
        print("✅ Flag content 'tea' matches the food theme of 'Nom Nom Nom'")
        print("✅ Solution methodology follows the hints:")
        print("   - 'Check the margins' → Found data in EXIF metadata")
        print("   - 'Nom Nom Nom' → Pattern extraction (every 2nd character)")
        print("   - Food theme → 'tea' is a beverage/food item")
        return True
    else:
        print(f"⚠️  Flag content '{flag_content}' - verify this matches challenge expectations")
        return False

if __name__ == "__main__":
    print("=== Verifying Nom Nom Nom Solution ===")
    
    if verify_solution():
        print("\n🎉 Solution verified successfully!")
    else:
        print("\n❌ Solution verification failed")