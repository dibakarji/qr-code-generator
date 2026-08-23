# QR Code Generator 📱

Generate QR code PNG images from any text or URL, straight from the terminal.

## Features

- Auto-sizes the QR matrix for the data length
- Custom foreground/background colors (`--fill`, `--back`)
- Adjustable module size (`--box-size`) for crisp prints
- Medium error correction - survives minor scuffs and logos

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python generate_qr.py "https://github.com/dibakarji"
python generate_qr.py "WiFi:MyNetwork" -o wifi.png --fill navy
python generate_qr.py "Hello!" --box-size 20 -o poster_qr.png
```

## Example

```
$ python generate_qr.py "https://github.com/dibakarji" -o github.png
QR code saved to C:\projects\qr-code-generator\github.png
```

---
Part of my **31 Python Projects** challenge - one small, genuine project at a time.
