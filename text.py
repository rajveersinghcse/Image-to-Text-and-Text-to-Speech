from gtts import gTTS #text to speech convertion
import pytesseract
import os
from PIL import Image
import cv2

img=cv2.imread("download.png")
cv2.imshow('input image',img)
print(img.shape)
print(img.size)
print(type(img))

img = cv2.resize(img,(200,250))
cv2.imshow('resized image',img) #to show the image in text
cv2.imwrite('img.png',img)
cv2.imshow('new',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
ret,bw=cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('black and white',bw)

#image to text
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
result=pytesseract.image_to_string(img)
print(result)

##text to speech
speach=gTTS(text=result,lang='en',slow=False)
speach.save('speach.mp3')
os.system('speach.mp3')