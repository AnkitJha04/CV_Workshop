import cv2
import numpy as np 

image = cv2.imread("sample.jpg")          
resize = cv2.resize(image,(200,200))
avg_blur = cv2.blur(image, (7,7))

def put_label(img,text,pos=(10,25)):
    return cv2.putText(img,text,pos, cv2.FONT_HERSHEY_SIMPLEX,0,6,(0,255,0),2)

org_lbl = put_label(image.copy(),"Original label ")
resize_lbl = put_label(image.copy(),"Resize label ")
average_lbl = put_label(image.copy(),"Average label ")

cv2.imshow('Original image',image)
cv2.imshow('Average image',image)
cv2.imshow('Resize image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()