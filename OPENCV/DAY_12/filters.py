#import required library
import cv2

#read image
image = cv2.imread("OPENCV/DAY_12/sample.jpeg")

#gaussian blur
gaussian = cv2.GaussianBlur(image,(5,5),0)

#median blur
median = cv2.medianBlur(image,5)

#bilateral filter
bilateral = cv2.bilateralFilter(image,9,75,75)

#display original image
cv2.imshow("Original Image", image)

#display gaussian blur
cv2.imshow("Gaussian Blur", gaussian)

#display median blur
cv2.imshow("Median Blur", median)

#display bilateral filter
cv2.imshow("Bilateral Filter", bilateral)

#wait for key press
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()