import cv2
import numpy as np
import random

height, width = (500, 500)
blank_img = np.zeros((height, width, 3), np.uint8)

for row in blank_img[:, :width, 1]:
    for element in range(len(row)):
        row[element] = random.choice([0, 255])
        
row_random = random.randint(0, 100)
row_thickness = random.randint(5, 50)
purple_width = random.randint(260, 490)

blank_img[row_random:(row_random+row_thickness), row_random:(row_random+purple_width)] = [255, 0, 255]

no_scratches = 5
for _ in range(random.randint(0, no_scratches)):
    row_random = random.randint(150, 400)
    blank_img[row_random: (row_random + random.randint(1, 3)), row_random: (row_random+random.randint(35, 70))] = [192, 192, 192]

non_glare = blank_img

image_lab = cv2.cvtColor(blank_img, cv2.COLOR_BGR2GRAY)
l_channel, a, b = cv2.split(image_lab)
clahe = cv2.createCLAHE()
cl = clahe.apply(l_channel)



cv2.imshow("Image", blank_img)
cv2.waitKey()