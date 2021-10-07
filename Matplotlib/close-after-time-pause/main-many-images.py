import matplotlib.pyplot as plt
import numpy as np

for _ in range(5):

    X = np.random.rand(10,10)

    plt.imshow(X)

    plt.show(block=False)
    plt.pause(3)

plt.close("all")
