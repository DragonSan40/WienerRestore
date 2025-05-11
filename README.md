# 🧼 WienerRestore

A simple Python tool to demonstrate **image restoration** using **Wiener deconvolution**. This script simulates motion blur on a grayscale image and then attempts to restore it using a known Point Spread Function (PSF).

---

## 📌 Features

* Select image using a file dialog (`tkinter`)
* Simulate blur using a uniform 5x5 kernel (PSF)
* Apply Wiener deconvolution for image restoration
* Compare original, blurred, and restored images side-by-side

---

## 📷 Example Output

| Original                          | Blurred                         | Restored (Wiener)                 |
| --------------------------------- | ------------------------------- | --------------------------------- |
| ![original](example_original.png) | ![blurred](example_blurred.png) | ![restored](example_restored.png) |

> *(Add example images to your repo to make this section work)*

---

## ⚙️ Requirements

Make sure the following packages are installed:

```bash
pip install opencv-python scikit-image matplotlib scipy
```

---

## 🚀 Usage

```bash
python wiener_restore.py
```

1. A file dialog will open. Select an image (JPG, PNG, BMP, etc.).
2. The image is converted to grayscale and blurred using a box filter.
3. Wiener deconvolution is applied to restore the image.
4. The result is displayed in a matplotlib window.

---

## 📁 File Structure

```
wiener_restore.py
README.md
example_original.png
example_blurred.png
example_restored.png
```

---

## 📝 Notes

* Input image is converted to float and normalized to \[0, 1] before processing.
* You can tweak the PSF size and Wiener `balance` parameter to experiment with different restoration results.
