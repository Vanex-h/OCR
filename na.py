import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image, grayscale, apply sharpening filter, Otsu's threshold 
image = cv2.imread('water-meter-reading.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpen_kernel = np.array([[-11,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# OCR
data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')

# cv2.imshow('sharpen', sharpen)
# cv2.imshow('thresh', thresh)
img = cv2.imread('water-meter-reading.jpg') 

# Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('thresholded', gray_image)
cv2.waitKey()
# Use Tesseract to do OCR on the grayscale image
extracted_text = pytesseract.image_to_string(gray_image, lang='eng', config='--psm 6')

# Filter extracted text to keep only numeric characters
numbers = ''.join(filter(str.isdigit, extracted_text))

# Print extracted numbers
print(extracted_text)




