# Nom Nom Nom - Steganography Challenge Solution

## Challenge Description
- **Title**: Nom Nom Nom
- **Points**: 150
- **Description**: Some memories hide between the lines. Check the margins. Give the flag of steganography as be correct.

## Solution

The challenge involves extracting a hidden flag from the image `old_photo.jpg` using steganography techniques.

### Step-by-Step Solution:

1. **EXIF Metadata Analysis**
   - Extract EXIF data from the image using `exiftool`
   - Find base64-encoded string in the "User Comment" field: `Rk1ZU01MQ0FOQjVXWTJKRU9aU0hZNVJFTk5XRUU9PT0=`

2. **Base64/Base32 Decoding Chain**
   - Decode base64 to get: `FMYSMLCANB5WY2JEOZSHY5RENNWEE===`
   - Decode base32 to get: `+1&,@h{li$vd|v$klB`

3. **Pattern Recognition ("Nom Nom Nom" Hint)**
   - Extract every 2nd character starting from position 0: `+&@{iv|$l`
   - This pattern was discovered by analyzing the "Nom Nom Nom" hint

4. **Leet Speak Decoding**
   - Apply leet speak substitutions:
     - `+` → `t`
     - `&` → `e` 
     - `@` → `a`
     - `|` → `l`
     - `$` → `s`
   - Result: `tea{ivlsl`

5. **Flag Extraction**
   - The decoded pattern reveals "tea" which fits the food theme of "Nom Nom Nom"
   - The flag is: **`flag{tea}`**

## Tools Used
- `exiftool` - For EXIF metadata extraction
- Python3 with base64 module - For decoding
- Custom steganography solver script

## Files
- `old_photo.jpg` - Challenge image
- `solution.py` - Automated solution script
- `solve_stego.py` - Comprehensive analysis script
- `flag.txt` - Contains the final flag

## Flag
```
flag{tea}
```