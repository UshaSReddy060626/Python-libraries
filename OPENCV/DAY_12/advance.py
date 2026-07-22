#video capture
import cv2

#for webcam
cap = cv2.VideoCapture(0)

#for video file
#cap = cv2.VideoCapture("testvideo.mp4")

#read frame
success, frame = cap.read()

#convert frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#gaussian blur
gaussian = cv2.GaussianBlur(frame, (5,5), 0)

#median blur
median = cv2.medianBlur(frame, 5)

#bilateral filter
bilateral = cv2.bilateralFilter(frame, 9, 75, 75)

#edge detection
edges = cv2.Canny(gray, 100, 200)

#binary threshold
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#adaptive threshold
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#draw contours
output = frame.copy()
cv2.drawContours(output, contours, -1, (0,255,0), 2)

#release video
cap.release()

#close windows
cv2.destroyAllWindows()