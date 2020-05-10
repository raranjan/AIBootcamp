import socket
import imagezmq
import cv2

sender = imagezmq.ImageSender(connect_to='tcp://localhost:5555')

sender_name = socket.gethostname() # send your hostname with each image
print(sender_name)

cap = cv2.VideoCapture(0)

while True:  # send images as stream until Ctrl-C
    ret, frame = cap.read()

    scale_percent = 60 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    # cv2.imshow("Rakesh", frame)
    if ret == True:
        sender.send_image(sender_name, frame)

    if cv2.waitKey(1) == 27: 
            break  # esc to quit

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()