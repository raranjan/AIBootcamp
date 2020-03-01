import cv2
from sklearn.cluster import KMeans

img_path = '/Users/rakesh/Workspace/AIBootcamp/data/paris.jpeg'
limit_image_size = 0
stroke_scale = 0
gradient_smoothing_radius = 0
palette_size = 20

img = cv2.imread(img_path)
print(img.shape)

# Convert image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

