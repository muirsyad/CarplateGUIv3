import cv2 as cv
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\Tesseract-OCR\\tesseract.exe'

def gray(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def noise_rem(image):
    kernal = np.ones((1,1), np.uint8)
    image= cv.dilate(image,kernal,iterations=1)
    kernal = np.ones((1,1),np.uint8)
    image=cv.erode(image,kernal,iterations=1)
    image=cv.morphologyEx(image,cv.MORPH_CLOSE,kernal)
    image=cv.medianBlur(image,3)
    return (image)

def ocr_base(image):
    text = pytesseract.image_to_string(image)
    return text

def carP(plate,tess):
    if plate == tess:
        print("SUCC")
        return plate
    else:
        print("INVALID")


img=cv.imread("c1.jpg")
cv.imshow("ori",img)


print('Original Dimensions : ', img.shape)

scale_percent = 300  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv.imshow("Resized image", resized)


#invert images
inv_img=cv.bitwise_not(resized)
cv.imwrite("inv.jpg",inv_img)
cv.imshow("INV", inv_img)


#gray
gray_img=gray(inv_img)
cv.imwrite("gray.jpg",gray_img)
cv.imshow("gray",gray_img)


thresh, im_bw=cv.threshold(gray_img, 180, 200, cv.THRESH_BINARY)
cv.imwrite("bw_image.jpg", im_bw)
cv.imshow("bw",im_bw)


#noise
no_noise=noise_rem(im_bw)
cv.imwrite("No.jpg",no_noise)
cv.imshow("no noise",no_noise)


tess=ocr_base(no_noise)
print(tess)
cv.waitKey(0)
carplate1=tess
carplate2="tess"
carplate1=carP(carplate1,tess)
carplate2=carP(carplate2,"tess")

print(carplate1)
print(carplate2)