# Watermark Maker

A simple desktop application built with Python and Tkinter that allows users to add text watermarks to images.

## Features

- Upload images (supports PNG, JPG, JPEG, BMP, and GIF formats)
- Add custom text watermarks
- Preview watermarked images
- Save watermarked images in PNG or JPEG format
- User-friendly graphical interface

## Requirements

- Python 3.x
- Pillow (PIL Fork)

## Installation

1. Clone this repository or download the source code:
```bash
git clone https://github.com/whizdome/watermark_adder.git
cd watermark_adder
```

2. Install the required dependencies:
```bash
pip install Pillow
```

## Usage

1. Run the application:
```bash
python watermark_maker.py
```

2. Use the application:
   - Click "Upload Image" to select an image file
   - Enter your desired watermark text in the text field
   - Click "Add Watermark" to apply the watermark
   - Click "Save Image" to save your watermarked image

## How It Works

The application uses:
- Tkinter for the graphical user interface
- PIL (Python Imaging Library) for image processing
- The watermark is added to the bottom-right corner of the image
- Watermark text is semi-transparent (50% opacity)

## License


## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Author

Wisdom