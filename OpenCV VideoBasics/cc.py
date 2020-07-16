import cv2

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

#WINDOWS = *'DIVX'
#MACOS OR LINUX = *'XVID'

writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc(*"XVID"), 20,(width,height))

while True :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release()
cv2.destroyAllWindows()