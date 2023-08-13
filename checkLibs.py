import os

# pip install Pillow PyMuPDF pytesseract

def checkLibs():
    libs = []
    try:
        import PIL
    except:
        print("❌❌❌ Error: PIL not installed ❌❌❌")
        libs.append("Pillow")
    try:
        import fitz
    except:
        print("❌❌❌ Error: fitz not installed ❌❌❌")
        libs.append("PyMuPDF")
    try:
        import pytesseract
        if not os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe'):
            print("❌❌❌ Error: Tesseract Location not default\nPlease move it to C:\\Program Files\\Tesseract-OCR ❌❌❌")
    except:
        print("❌❌❌ Error: pytesseract not installed ❌❌❌")
        libs.append("pytesseract")
    
    if len(libs) > 0:
        print("✅✅✅ Please run the following command ✅✅✅: ", end="")
        print("pip install " + " ".join(libs))
        return False
    else:
        return True
    

if checkLibs(): # Check if all libraries are installed
    print("✅✅✅ All libraries are installed ✅✅✅")

    