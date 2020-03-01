import cv2
from sklearn.cluster import KMeans

img_path = '/Users/rakesh/Workspace/AIBootcamp/data/paris.jpeg'

def show_image(gray=True):
    img = cv2.imread(img_path)

    # Convert image to gray scale
    if gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_image()

