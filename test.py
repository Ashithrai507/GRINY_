from PIL import Image
import numpy as np

img = Image.open("demo.jpg").convert("RGB")
width, height = img.size
pixels = img.load()

binary_image = []   # will store all pixels' binary data

for y in range(height):
    row_bits = []
    for x in range(width):
        r, g, b = pixels[x, y]

        # Convert RGB → bits (0/1)
        bits = np.unpackbits(
            np.array([r, g, b], dtype=np.uint8)
        )

        row_bits.append(bits)
    binary_image.append(row_bits)

# Example: print first pixel bits
print(binary_image[0][0])
