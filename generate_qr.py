#!/usr/bin/env python3
"""Generate QR codes from text or URLs directly from the command line."""

import argparse
from pathlib import Path

import qrcode


def make_qr(data: str, output: Path, fill: str, back: str, box_size: int):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(output)
    return img


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code image")
    parser.add_argument("data", help="Text or URL to encode")
    parser.add_argument("-o", "--output", default="qr_code.png",
                        help="Output PNG path (default: qr_code.png)")
    parser.add_argument("--fill", default="black", help="Foreground color (default: black)")
    parser.add_argument("--back", default="white", help="Background color (default: white)")
    parser.add_argument("--box-size", type=int, default=10,
                        help="Pixel size of each box (default: 10)")
    args = parser.parse_args()

    output = Path(args.output)
    if output.suffix.lower() != ".png":
        parser.error("Output must be a .png file")

    make_qr(args.data, output, args.fill, args.back, args.box_size)
    print(f"QR code saved to {output.resolve()}")


if __name__ == "__main__":
    main()
