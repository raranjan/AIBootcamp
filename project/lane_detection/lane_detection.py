import cv2
import numpy as np

PATH = './data/test_image.png'


def display_image(image):
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def edge_detection(image):
    # Covert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise from image
    blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
    canny = cv2.Canny(blur, 20, 80)

    return canny

def canny_edge_detector(image):
    pass

if __name__ == '__main__':
    image = cv2.imread(PATH)
    updated_image = edge_detection(image)
    display_image(updated_image)
