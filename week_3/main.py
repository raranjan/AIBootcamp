import cv2
import imutils

dog = cv2.imread("data/dog.jpg")


def image_proc_pipeline(img):
    resized = imutils.resize(img, height=500)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 8)

    edge = cv2.Canny(blur, 75, 200)

    return resized, edge


def video_capture():
    video = cv2.VideoCapture(0)

    while video.isOpened():
        ret, frame = video.read()

        if ret == True:
            resize, result = image_proc_pipeline(frame)

            cv2.imshow("resized", resize)
            cv2.imshow("result", result)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_capture()
