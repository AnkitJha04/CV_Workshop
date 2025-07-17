import cv2

image = cv2.imread("sample.jpg")
                    
cv2.imshow('Original image',image)
cv2.resize(image,(200,200))
cv2.rotate(image,cv2.ROTATE_180)
image[100:300,200:400]
flip = cv2.flip (image,1)
cv2.waitKey(0)
cv2.destroyAllWindows()