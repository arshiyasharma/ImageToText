# ImageToText
Using the easyocr and pytesseract libs to extract text from image

# Important installations
### • Virtual Environment:
                
    > pip install pytesseract
  
    > pip install tesseract
   
    > pip install Pillow
  
    > pip install easyocr
  
    > pip install 
  
### • If you're on windows:

  **Step 1:** Download tesseract exe using : https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe
  
  **Step 2:** Type these commands in the .py file before running it.
         
    > ocr_path = r"--the path to the tesseract.exe present in tesseractOCR folder in program files in User--"
          
    > pyt.pytesseract.tesseract_cmd = ocr_path
  
  
### • If you're using macOs and it gives you any errors regarding tesseract, please use Homebrew to download the library:
  Link : https://brew.sh
  
  after installation, run
  
    > brew install tesseract
  
# How it operates
**Step 1:** Change the name of your image to 'ocr' and make sure that it's either png or jpg.

**Step 2:** Open the project in your compiler.

**Step 3:** Add the image in the project (no folder, just drag and drop).

**Step 3:** On running either *jpgToText.py* or *pngToText.py* depending on the file, you will get a file named **'ocr.txt'**. If you run the code again, it will *overwrite* the file.

##

Project By : Arshiya Sharma

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
