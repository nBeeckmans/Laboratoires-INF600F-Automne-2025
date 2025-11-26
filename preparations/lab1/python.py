from skimage import io
import numpy as np
import matplotlib.pyplot as plt


image = io.imread("image.png")
imageAsArray = np.array(image)
print(imageAsArray.shape)

io.imsave("image2.png", imageAsArray)

