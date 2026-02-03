from PIL import Image
import numpy as np

img = Image.open("demo.jpg").convert("RGB")
pixel_array = np.array(img)
height, width, _ = pixel_array.shape

with open("pixel_values.txt", "w") as file:
    file.write(f"Image Size: {width} x {height}\n")
    file.write("Format: (x, y) -> R G B\n\n")

    for y in range(height):
        for x in range(width):
            r, g, b = pixel_array[y, x]
            
            file.write(f"({x},{y}) -> {r} {g} {b}\n")

print("All pixel RGB values stored in pixel_values.txt")
