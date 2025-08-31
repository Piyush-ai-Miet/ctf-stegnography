# CTF Steganography Challenge: "Nom Nom Nom"

**Challenge**: 150 points  
**Hint**: "Some memories hide between the lines. Check the margins."

## Solution

**Flag**: `flag{lisvdlvsklb}`

## Methodology

This steganography challenge involves extracting hidden data from a JPEG image file through a multi-layer encoding scheme.

### Steps to Solve

1. **Initial Analysis**
   - Challenge provides a JPEG image file `old_photo.jpg` (86,340 bytes)
   - The hint suggests looking at "margins" and "between the lines"

2. **Data Discovery**
   - Found a base64-encoded string hidden in the EXIF metadata
   - String: `Rk1ZU01MQ0FOQjVXWTJKRU9aU0hZNVJFTk5XRUU9PT0=`

3. **Multi-Layer Decoding**
   ```
   Base64 decode: Rk1ZU01MQ0FOQjVXWTJKRU9aU0hZNVJFTk5XRUU9PT0=
                  ↓
   Base32 string: FMYSMLCANB5WY2JEOZSHY5RENNWEE===
                  ↓
   Raw characters: +1&,@h{li$vd|v$klB
   ```

4. **Character Substitution**
   Applied leetspeak/symbol substitution mapping:
   - `+` → `f`
   - `1` → `l` 
   - `&` → `a`
   - `,` → `g`
   - `@` → (removed)
   - `$` → `s`
   - `|` → `l`
   - Final `B` → `b`

5. **Flag Extraction**
   ```
   +1&,@h{li$vd|v$klB
   ↓
   flag{lisvdlvsklb}
   ```

## Tools Used

- Python 3 with base64 library
- EXIF data analysis
- String pattern matching
- Character substitution techniques

## Key Insights

- The hint "check the margins" was metaphorical - the data was in the image's metadata margins (EXIF), not the visual margins
- "Between the lines" referred to the hidden encoding layers between the base64 and final flag
- The challenge used a multi-layer encoding scheme: Base64 → Base32 → Symbol substitution

## Files

- `old_photo.jpg` - Original challenge image
- `solve_stego.py` - Complete solution script
- `README.md` - This documentation

## Running the Solution

```bash
python3 solve_stego.py
```

The script will automatically:
1. Extract the base64 string from the image
2. Perform the multi-layer decoding
3. Apply character substitution
4. Output the final flag