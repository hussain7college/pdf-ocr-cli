from pytesseract import image_to_string 


def img_to_text(img, lang="eng"):
    try:
        text = image_to_string(img, lang=lang)
        text = text.replace("‎", "")
        text = text.replace("‏", "")
        return text
    except Exception as e:
        print("❌❌❌", e)
        return False
    
# print(image_to_string("debug/page_0.png")) # OCR image