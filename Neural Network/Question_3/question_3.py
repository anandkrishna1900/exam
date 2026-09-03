# Question 3: Visualize activation functions (Sigmoid vs ReLU) using plots.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)

plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.legend()
plt.show()
