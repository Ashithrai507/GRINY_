from PIL import Image
import numpy as np
import math

# -----------------------------
# 1. Load image
# -----------------------------
img = Image.open("img.jpg").convert("RGB")
width, height = img.size
pixel_array = np.array(img, dtype=np.uint8)  # (H, W, 3)

# -----------------------------
# 2. Convert RGB → bitstream
# -----------------------------
binary_pixels = np.unpackbits(pixel_array, axis=2)  # (H, W, 24)
bitstream = binary_pixels.flatten()                  # 1D array

total_bits = len(bitstream)

# -----------------------------
# 3. Pad bitstream to multiple of 8
# -----------------------------
pad_len = (8 - (total_bits % 8)) % 8
if pad_len > 0:
    bitstream = np.pad(bitstream, (0, pad_len), constant_values=0)

# -----------------------------
# 4. Pack 8 bits → 1 byte
# -----------------------------
byte_array = np.packbits(bitstream)  # values 0–255

# -----------------------------
# 5. Create encrypted grayscale image
# -----------------------------
enc_width = 512  # can choose any reasonable width
enc_height = math.ceil(len(byte_array) / enc_width)

# Pad bytes if needed
pad_pixels = enc_width * enc_height - len(byte_array)
if pad_pixels > 0:
    byte_array = np.pad(byte_array, (0, pad_pixels), constant_values=0)

encrypted_array = byte_array.reshape(enc_height, enc_width)

encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8), mode="L")
encrypted_img.save("encrypted_noise.png")

# -----------------------------
# 6. Save metadata
# -----------------------------
with open("metadata.txt", "w") as f:
    f.write(f"original_width={width}\n")
    f.write(f"original_height={height}\n")
    f.write("channels=3\n")
    f.write("bits_per_pixel=24\n")
    f.write(f"total_bits={total_bits}\n")
    f.write(f"encrypted_width={enc_width}\n")

print("✅ Encryption complete (8-bit packed)")
