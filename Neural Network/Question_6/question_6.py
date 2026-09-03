# Question 6: Backpropagation for a simple neural network.

import torch

x = torch.tensor(2.0, requires_grad=True)

y = x**2 + 3*x + 1
y.backward()

print("Gradient:", x.grad)
