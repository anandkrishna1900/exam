# Question 1: Implement a basic neural network using TensorFlow or PyTorch.

import torch
import torch.nn as nn

X = torch.tensor([[1.0], [2.0], [3.0]])
y = torch.tensor([[2.0], [4.0], [6.0]])

model = nn.Linear(1, 1)

loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    output = model(X)
    loss = loss_fn(output, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

prediction = model(torch.tensor([[4.0]]))
print("Predicted Output:", prediction.item())
