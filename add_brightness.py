import numpy as np
import cv2

img1 = cv2.imread('./scenery.jpg')
img2 = cv2.imread('./light.jpg')
white_channel = np.ones(img1.shape) * 100 
white_channel2 = np.ones(img2.shape) * 100 
new_image = np.array(white_channel + img1).clip(0, 255)
new_light = np.array(white_channel2 - img2).clip(0, 255)

cv2.imwrite('./new_scenery.jpg', new_image)
cv2.imwrite('./light.jpg', new_image)

