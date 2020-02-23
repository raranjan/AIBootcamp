import cv2
from sklearn.cluster import KMeans

img_path = 'paris.jpeg'

def show_image(gray=True):
    img = cv2.imread(img_path)

    # Convert image to gray scale
    if gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_webcam():
    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) == 27:
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_image()
    show_webcam()

