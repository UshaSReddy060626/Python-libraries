#import required library
import cv2

#read image
image = cv2.imread("OPENCV/DAY_12/sample.jpeg")

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect edges
edges = cv2.Canny(gray,100,200)

#apply binary threshold
ret, binary = cv2.threshold(gray,127,255,
cv2.THRESH_BINARY)

#find contours
contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#draw contours
output = image.copy()

cv2.drawContours(output,contours,-1,(0,255,0),2)

#display images
cv2.imshow("Original Image", image)
cv2.imshow("Edge Detection", edges)
cv2.imshow("Binary Threshold", binary)
cv2.imshow("Contours", output)

#wait for key press
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()