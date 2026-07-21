import cv2
image=cv2.imread("OPENCV/DAY_11/pic.jpg", 0)
cv2.imshow("picture",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("copyof_pic.jpg",image)
print(image.shape)
print(image.size)
print(image.dtype)
