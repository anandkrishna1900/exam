# Question 8: Train a basic classifier.

import torch
import torch.nn as nn
import torch.optim as optim

X = torch.tensor([[1.0],
                  [2.0],
                  [3.0],
                  [4.0]])

y = torch.tensor([[0.0],
                  [0.0],
                  [1.0],
                  [1.0]])

model = nn.Sequential(
    nn.Linear(1, 1),
    nn.Sigmoid()
)

criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(100):
    outputs = model(X)
    loss = criterion(outputs, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    predictions = model(X)
    print("Predicted Probabilities:")
    print(predictions)
    print("\nPredicted Classes:")
    print((predictions > 0.5).float())
