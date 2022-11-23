import cv2, matplotlib.pyplot as plt, numpy as np

IMG_NAME = "img2.jpeg"

colors = cv2.imread(IMG_NAME)
plt.imshow(colors[:,:,[2,1,0]])
plt.show()
