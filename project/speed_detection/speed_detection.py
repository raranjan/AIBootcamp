import numpy as np
import cv2
from logzero import logger
import imagehash

cap = cv2.VideoCapture("/Users/rakesh/Workspace/AIBootcamp/project/speed_detection/data/train.mp4")
previous_frame = None
dot_product = []
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret == False:
        logger.info('Unable to open the video')
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    if previous_frame is None:
        previous_frame = blur
    else:

        previous_frame = blur

    # Display the resulting frame
    cv2.imshow('frame', blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()