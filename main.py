import checkLibs # Check if all required libraries are installed
from pdf2img import pdf_to_images
from img2text import img_to_text
import os

def ocrFile(inputFile, outputFile, lang="eng"):
    images = pdf_to_images(inputFile)
    ocr_text = ""
    
    print("🔃🔃🔃 OCR PDF ... 🔃🔃🔃")
    for idx, img in enumerate(images):
        print(f"🔃🔃🔃 OCRing page ({idx}) of ({len(images)})")
        ocr_result = img_to_text(img, lang)
        if ocr_result:
            ocr_text += f"------------📄 Page ({idx}) 📄------------\n"
            ocr_text += ocr_result + "\n"
        else:
            print(f"❌❌❌ Error processing page ({idx}) ❌❌❌")
    
    print(f"Done OCRing PDF ({inputFile})")
    print("🔃🔃🔃 Saving OCR text to file ... 🔃🔃🔃")
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write(ocr_text)
    print(f"✅✅✅ Done saving OCR text to file ({outputFile}")
          

def ocrFiles(inputDirectory, outputDirectry, lang):
    for fileName in os.listdir(inputDirectory):
        if fileName.endswith(".pdf"):
            inputFilePath = inputDirectory+"\\"+fileName
            outputFilePath = outputDirectry + "\\" + fileName[:-4] + ".txt"
            ocrFile(inputFilePath, outputFilePath, lang)

def createDirectories():
    if not os.path.exists("in"):
        os.makedirs("in")
    if not os.path.exists("out"):
        os.makedirs("out")


if __name__ == "__main__":
    while(True):
        createDirectories()
        lang = input("Enter language (ara, eng): ")
        ocrFiles("in", "out", lang)
        print("✅✅✅ Done ✅✅✅\n\n")
    
