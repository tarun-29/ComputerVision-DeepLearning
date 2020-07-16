import cv2
import time

cap = cv2.VideoCapture("../DATA/mysupervideo.mp4")

if cap.isOpened()==False :
    print("Error file not found OR Wrong codec used")

while cap.isOpened():
    ret,frame = cap.read()
    
    if ret==True:
        time.sleep(1/20)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

    else :
        break

cap.release()
cv2.destroyAllWindows()