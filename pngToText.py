import pytesseract as pyt

extracted_text = pyt.image_to_string('ocr.png')

file = open('ocr.txt', 'w')  # modes - r=read w=read,write(overwrites) a=read,write,append(adds to prev text)
file.write(extracted_text)
file.close()
print("Text Extracted Successfully")
