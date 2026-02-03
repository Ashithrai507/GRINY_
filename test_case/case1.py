# ...existing code...
from PIL import Image
import numpy as np
import os
import sys

# Use script directory so relative runs work reliably
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, "demo.jpg")
out_dir = os.path.join(BASE_DIR, "bit_planes")

# Load image
try:
    img = Image.open(img_path).convert("RGB")
except FileNotFoundError:
    print(f"Error: image not found at {img_path}", file=sys.stderr)
    sys.exit(2)
except Exception as e:
    print("Error opening image:", e, file=sys.stderr)
    sys.exit(3)

# Convert image to NumPy array
pixel_array = np.array(img, dtype=np.uint8)  # shape (H, W, 3)

# Convert RGB → binary (expand each byte to 8 bits). explicit bitorder
binary_image = np.unpackbits(pixel_array, axis=2, bitorder="big")  # (H, W, 24)

height, width, bits = binary_image.shape
if bits != 24:
    print(f"Unexpected bit depth: {bits} (expected 24)", file=sys.stderr)

# Create output folder
os.makedirs(out_dir, exist_ok=True)

# Generate 24 black & white images
saved = 0
for bit in range(bits):
    # Extract one bit-plane (0..23)
    bit_plane = binary_image[:, :, bit]

    # Convert 0/1 → 0/255
    bw_image = (bit_plane * 255).astype(np.uint8)

    # Save image into absolute out_dir
    out_path = os.path.join(out_dir, f"bit_{bit:02d}.png")
    Image.fromarray(bw_image, mode="L").save(out_path)
    saved += 1

print(f"✅ {saved} black & white bit-plane images saved in '{out_dir}'")
# ...existing code...