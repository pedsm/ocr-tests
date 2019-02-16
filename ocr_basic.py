try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

image_url = './mag_scan.png'
full_text = pytesseract.image_to_string(Image.open(image_url))
print(full_text)