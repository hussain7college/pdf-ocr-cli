import pytesseract  # Tesseract OCR library

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def img_to_text(img, lang="eng"):
    try:
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except Exception as e:
        print("❌❌❌", e)
        return False