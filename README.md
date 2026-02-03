# Binary Grain Image Encoding & Decoding System

##  Project Overview

This project implements a **custom reversible encoding algorithm** that converts a normal color image into a **black-and-white grain image** representing binary data (0s and 1s), and then decodes it back into the **original image without loss**.

The system demonstrates how digital images can be transformed into pure binary visual representations using a deterministic, rule-based approach.

---

##  Objectives

- Design a **custom encoding algorithm** from scratch
- Convert RGB image data into a **binary bitstream**
- Visually represent bits using **black and white grains**
- Decode the grain image back into the original image
- Ensure **lossless reconstruction**
- Understand low-level image representation and binary data handling

---

##  Core Concept

Every digital image is fundamentally composed of numbers, and every number can be represented in binary.

This project uses the mapping:
0 → Black pixel (0)
1 → White pixel (255)

Each pixel’s color information is converted into binary and stored visually as a black-and-white grain pattern.

---

##  System Architecture
```sscs
Original Image (RGB)
↓
Pixel Channel Extraction
↓
Binary Conversion (0s & 1s)
↓
Binary-to-Grain Mapping
↓
Black & White Grain Image
↓
(Binary Decoding)
↓
Reconstructed Image
```

---
## RGB(Red Blue Green)
RGB image can be viewed as three different images(a red scale image, a green scale image and a blue scale image) stacked on top of each other, and when fed into the red, green and blue inputs of a color monitor, it produces a color image on the screen. 

- RGB color model is the model in which Red, Blue, and Green colors are blended together to form an array of colors
- In this article, we will learn the concept of extraction of RGB components from an image and the calculation of RGB values pixels on the MATLAB interface.
- An RGB image is sometimes referred to as a true color image as the precision with which a real-life image can be replicated has led to the nickname “true color image.” 
---

##  Encoding Algorithm Design

### 1️ Input Format
- RGB image
- Lossless format recommended (PNG, BMP)

---

### 2️ Pixel Representation

Each pixel contains:
- Red channel (8 bits)
- Green channel (8 bits)
- Blue channel (8 bits)

Total:24 bits per pixel

```sscs
Example:
Pixel = (120, 45, 200)

R = 01111000
G = 00101101
B = 11001000

Combined Binary:
011110000010110111001000
```

---

### 3️ Bit-to-Grain Mapping

| Binary Bit | Grain Pixel |
|-----------|-------------|
| 0         | Black (0)   |
| 1         | White (255)|

Each bit is represented by **one grain pixel**.

---

### 4️ Output Image Layout

- **Output Width** = Input Width × 24
- **Output Height** = Input Height
- Bits are stored **left to right, row-wise**

This layout ensures simple and deterministic decoding.

---

##  Metadata Header

To ensure correct reconstruction, metadata is embedded at the start of the bitstream.

### Header Structure

| Field | Size |
|------|------|
| Image Width | 32 bits |
| Image Height | 32 bits |
| Pixel Data | Remaining bits |

The header is also encoded as grains.

---

##  Decoding Algorithm

Decoding is the exact inverse of encoding.

### Steps:

1. Read grain image pixels left to right
2. Convert:
   - White → 1
   - Black → 0
3. Read first 64 bits to extract:
   - Original width
   - Original height
4. Group remaining bits into chunks of 24
5. Convert each chunk back into:
   - Red (8 bits)
   - Green (8 bits)
   - Blue (8 bits)
6. Reconstruct the original image pixel-by-pixel

---

##  Lossless Guarantee

The system is **lossless** provided:
- Grain image is not resized
- No compression (JPEG) is applied
- Pixel values remain unchanged
- Exact decoding rules are followed

---

##  Limitations

- Encoded image size is significantly larger
- Any visual alteration breaks decoding
- Not resistant to noise or compression
- Designed for educational and experimental use

---

##  Possible Enhancements

- Block-based grains (2×2 or 4×4 per bit)
- Error detection (parity bits, checksums)
- Bit-plane visualization
- Compression before encoding
- Encryption-based bit shuffling
- Video frame encoding
- AI-assisted reconstruction

---

##  Testing Strategy

Test cases:
- 1×1 pixel image
- Solid colors (red, green, blue)
- Grayscale image
- Random noise image
- Edge cases (odd widths)

Successful decoding in all cases confirms correctness.

---

##  Technology Stack

- Language: Python / Java (implementation-dependent)
- Image Processing: OpenCV / PIL (optional)
- Formats: PNG, BMP

---

##  Learning Outcomes

- Binary representation of images
- Low-level data encoding
- Lossless data transformation
- Algorithm design thinking
- Reversible system design

---

## 🏁 Conclusion

This project proves that **any image can be converted into a pure black-and-white binary grain representation and reconstructed perfectly**, as long as deterministic encoding and decoding rules are followed.

It serves as a foundation for deeper exploration into compression algorithms, digital communication, and creative visual data encoding.

---

##  Author

Designed and implemented by **Ashith Rai**

---

##  License

This project is intended for educational and experimental use.



