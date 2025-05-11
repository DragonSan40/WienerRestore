from skimage.restoration import wiener
from skimage import img_as_float
from scipy.signal import convolve2d
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
import os

# Open file dialog to select an image
root = Tk()
root.withdraw()  # Hide the root window
image_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
)

if not image_path:
    print("No file selected.")
    exit()

if not os.path.exists(image_path):
    print(f"File not found: {image_path}")
    exit()

# Load grayscale image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error loading image!")
    exit()

# Convert to float [0, 1]
image_float = img_as_float(image)

# Create PSF (box blur kernel)
psf = np.ones((5, 5)) / 25

# Optionally simulate blur if the image is not blurred already
blurred = convolve2d(image_float, psf, 'same')

# Apply Wiener deconvolution
restored = wiener(blurred, psf, balance=0.1)

# Plot results
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].imshow(image_float, cmap='gray')
axs[0].set_title("Original Image")
axs[1].imshow(blurred, cmap='gray')
axs[1].set_title("Blurred Image")
axs[2].imshow(restored, cmap='gray')
axs[2].set_title("Restored Image (Wiener)")
for ax in axs:
    ax.axis('off')
plt.tight_layout()
plt.show()
