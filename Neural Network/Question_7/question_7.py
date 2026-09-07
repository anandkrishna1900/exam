# Question 7: Train the model using gradient descent. Plot loss vs epochs. Compare learning with different learning rates.

import torch
import matplotlib.pyplot as plt

x = torch.tensor(2.0)
y = torch.tensor(4.0)
learning_rates = [0.1, 0.01]

for lr in learning_rates:
    w = torch.tensor(0.0, requires_grad=True)
    losses = []
    
    for epoch in range(20):
        y_pred = w * x
        loss = (y_pred - y) ** 2
        losses.append(loss.item())
        loss.backward()
        
        with torch.no_grad():
            w -= lr * w.grad
        w.grad.zero_()
        
    plt.plot(losses, label=f"LR = {lr}")

plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Loss vs Epochs")
plt.legend()
plt.show()
