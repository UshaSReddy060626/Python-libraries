import cv2
cap=cv2.VideoCapture("OPENCV/DAY_12/testvideo.mp4")
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
while True:
    success,frame=cap.read()
    if not success:
        break
    # gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",frame)
    #for grayscale
    #cv2.imshow("video",gray_frame)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
