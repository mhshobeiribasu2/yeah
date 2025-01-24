
from flask import Flask, request, jsonify
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import pytesseract
import re
import tempfile
from preprocess import process_image

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    img = process_image(file)
    
    # Convert image to string using pytesseract
    text = pytesseract.image_to_string(img, lang='fas')  # 'fas' is the language code for Persian

    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)