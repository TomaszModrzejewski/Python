
import skimage.io as io
import matplotlib.pyplot as plt

image = io.imread("https://homepages.cae.wisc.edu/~ece533/images/lena.png")

plt.imshow(image)
plt.axis('off')
plt.annotate("Lena", (10, 20))
plt.savefig("output.png", bbox_inches='tight', pad_inches=0)

