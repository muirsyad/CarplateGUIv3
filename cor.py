import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\Tesseract-OCR\\tesseract.exe'

def ocr_base(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv.imread('car3.jpg')

#get grayscale image
def get_gray(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#noise removerl
def remove_noise(image):
    return cv.medianBlur(image,5)

#thresh
def thresh(image):
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY +cv.THRESH_OTSU)[1]

img=get_gray(img)
img=thresh(img)
img=remove_noise(img)

print(ocr_base(img))
