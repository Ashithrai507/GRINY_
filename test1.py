from PIL import Image
import numpy as np

# Load image
img = Image.open("demo.jpg").convert("RGB")

# Convert image to NumPy array
pixel_array = np.array(img, dtype=np.uint8)  # shape: (H, W, 3)
height, width, _ = pixel_array.shape

# Convert entire image to binary (0/1)
binary_image = np.unpackbits(pixel_array, axis=2)  # shape: (H, W, 24)

# Write to TXT file
with open("binary_pixels.txt", "w") as file:
    file.write(f"Image Size: {width} x {height}\n")
    file.write("Format: (x, y) -> 24-bit binary (R[8] G[8] B[8])\n\n")

    for y in range(height):
        for x in range(width):
            bits = binary_image[y, x]
            bit_string = "".join(map(str, bits))
            file.write(f"({x},{y}) -> {bit_string}\n")

print("✅ All pixel binary values stored in binary_pixels.txt")
