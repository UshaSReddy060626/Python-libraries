#importing opencv
import cv2

#reading images
image=cv2.imread("OPENCV/DAY_11/pic.jpg")

#show image
cv2.imshow("Image Window", image)

#gray_scale image
gray=cv2.imread("pic.jpg",0)

#dispaly images
cv2.imshow("picture",image)

#cv2 wait key
cv2.waitkey(0)

#cv2.destroy all windows
cv2.destroyAllWindows()

#save images
cv2.imwrite("new_image.jpg",image)

#image properties
#shape
print(image.shape)
#size
print(image.size)
#dtype
print(image.dtype)
#resizing
small=cv2.resize(image,(300,300))
# image cropping
crop=image[50:200,100:300]

#draw on images
#draw line
cv2.line(image,(50,50),(200,200),(255,0,0),2)
#draw rectangle
cv2.rectangle(image,(50,50),(200,200),(0,255,0),2)
#draw circle
cv2.circle(image,(150,150),50,(0,0,255),2)
#text
cv2.putText(image,"Hello",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
#color conversion
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)