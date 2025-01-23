import os
import re

import pytesseract

from preprocess import process_image

langs = "fas"  # Languages for OCR eng+fas
fileAddress = os.path.join(input_dir, filename)
img = process_image(fileAddress)
config = ''
text = str(pytesseract.image_to_string(img, lang=langs, config=config))

# Remove empty lines of text - s.strip() removes lines with spaces
text = os.linesep.join([s for s in text.splitlines() if s.strip()])