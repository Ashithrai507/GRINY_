from PIL import Image
import numpy as np

# -----------------------------
# 1. Load metadata
# -----------------------------
metadata = {}
with open("metadata.txt", "r") as f:
    for line in f:
        k, v = line.strip().split("=")
        metadata[k] = v

orig_width  = int(metadata["original_width"])
orig_height = int(metadata["original_height"])
total_bits  = int(metadata["total_bits"])
bits_per_pixel = int(metadata["bits_per_pixel"])

# -----------------------------
# 2. Load encrypted image
# -----------------------------
enc_img = Image.open("encrypted_noise.png").convert("L")
byte_array = np.array(enc_img, dtype=np.uint8).flatten()

# -----------------------------
# 3. Convert bytes → bitstream
# -----------------------------
bitstream = np.unpackbits(byte_array)

# Remove padding bits
bitstream = bitstream[:total_bits]

# -----------------------------
# 4. Rebuild pixel binary
# -----------------------------
binary_pixels = bitstream.reshape(
    orig_height,
    orig_width,
    bits_per_pixel
)

# -----------------------------
# 5. Binary → RGB
# -----------------------------
reconstructed = np.packbits(binary_pixels, axis=2)

reconstructed_img = Image.fromarray(
    reconstructed.astype(np.uint8),
    mode="RGB"
)
reconstructed_img.save("decrypted_image.png")

print("✅ Decryption complete")
