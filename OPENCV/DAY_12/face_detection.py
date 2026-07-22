#import required library
import cv2

#load haar cascade classifier
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#open video
cap = cv2.VideoCapture("OPENCV/DAY_12/testvideo.mp4")

while True:

    #read frame
    success, frame = cap.read()

    if not success:
        break

    #convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    #draw bounding boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

    #display video
    cv2.imshow("Face Detection", frame)

    #press q to quit
    if cv2.waitKey(1) == ord("q"):
        break

#release video
cap.release()

#close windows
cv2.destroyAllWindows()