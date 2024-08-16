import datetime

import checkLibs # Check if all required libraries are installed
from pdf2img import pdf_to_images
from img2text import img_to_text
import os

def ocrFile(inputFile, outputFile, lang="eng"):
    errorPages = []
    images = pdf_to_images(inputFile)
    ocr_text = ""
    
    print("🔃🔃🔃 OCR PDF ... 🔃🔃🔃")
    for idx, img in enumerate(images):
        # save image for debugging
        img.save(f"debug/page_{idx}.png")
        print(f"🔃🔃🔃 OCRing page ({idx}) of ({len(images)})")
        ocr_result = img_to_text(img, lang)
        if ocr_result:
            ocr_text += ocr_result + f"\n------------📄 Page ({idx+1}) 📄------------\n"
        else:
            ocr_text += f"\n❌❌❌ Error processing page ({idx+1}) ❌❌❌\n"
            print(f"❌❌❌ Error processing page ({idx+1}) ❌❌❌")
            errorPages.append(idx+1)
    
    print(f"Done OCRing PDF ({inputFile})")
    print("🔃🔃🔃 Saving OCR text to file ... 🔃🔃🔃")
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write(ocr_text)
    print(f"✅✅✅ Done saving OCR text to file ({outputFile}")
    return errorPages
          

def ocrFiles(inputDirectory, outputDirectry, lang):
    for fileName in os.listdir(inputDirectory):
        if fileName.endswith(".pdf"):
            inputFilePath = os.path.join(inputDirectory, fileName)
            outputFilePath = os.path.join(outputDirectry, fileName[:-4] + ".txt")
            if os.path.exists(os.path.dirname(outputFilePath)):
                outputFilePath = renameUnique(outputFilePath)
            errorPages = ocrFile(inputFilePath, outputFilePath, lang)
            moveRenameFile(inputFilePath, os.path.join("done", fileName)) # move file to done folder
            if len(errorPages) > 0:
                print(f"❌❌❌ Error processing pages ({errorPages}) in file ({fileName}) ❌❌❌")

def moveRenameFile(src, dst):
    if os.path.exists(dst):
        os.rename(src, renameUnique(dst))
        return
    os.rename(src, dst)

def renameUnique(path):
    # rename file and keep extension
    [name, ext] = os.path.splitext(path)
    print("🍏🍏🍏🍏",name, ext)
    return name + "-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ext
    
       

def createDirectories():
    if not os.path.exists("in"):
        os.makedirs("in")
    if not os.path.exists("out"):
        os.makedirs("out")
    if not os.path.exists("done"):
        os.makedirs("done")

def chooseLanguage():
    print('''list of languages:
              1: Arabic
              2: English
              3: Arabic + English''')
    lang = int(input("Enter language (ara, eng): ").strip())
    if lang == 1:
        return "ara"
    elif lang == 2:
        return "eng"
    elif lang == 3:
        return "ara+eng"
    else:
        print("❌❌❌ Error: Invalid language ❌❌❌")
        return False

if __name__ == "__main__":
    while(True):
        createDirectories()
        lang = chooseLanguage()
        if (lang):
            ocrFiles("in", "out", lang)
            print("✅✅✅ Done ✅✅✅\n\n")
    
