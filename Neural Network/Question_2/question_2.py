# Question 2: Implement single artificial neuron using NumPy (with weights, bias and input).

import numpy as np

x = np.array([2])
w = np.array([3])
b = 1

y = x * w + b
print("Output =", y)
