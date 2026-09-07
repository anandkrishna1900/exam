# Question 4: Implement Feedforward neural network (FFNN). Perform forward propagation for a given dataset.

import torch
import torch.nn as nn

X = torch.tensor([[1.0],
                  [2.0],
                  [3.0],
                  [4.0]])

model = nn.Sequential(
    nn.Linear(1, 2),
    nn.ReLU(),
    nn.Linear(2, 1)
)

output = model(X)
print("Output:")
print(output.detach().numpy())
