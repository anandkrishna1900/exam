# Question 18: Image classification using a CNN in PyTorch.

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Create a simple CNN model
model = nn.Sequential(
    # Extract image features
    nn.Conv2d(1, 8, kernel_size=3),
    # Add non-linearity
    nn.ReLU(),
    # Reduce feature map size
    nn.MaxPool2d(2),
    # Convert feature maps into a vector
    nn.Flatten(),
    # Classify into 10 classes
    nn.Linear(8 * 13 * 13, 10)
)

# Create a random 28 x 28 grayscale image
image = torch.randn(1, 1, 28, 28)

# Display the image
plt.imshow(image.squeeze().numpy(), cmap="gray")
plt.title("Input Image")
plt.show()

# Pass image through the CNN
output = model(image)

# Display output shape
print("Output Shape :", output.shape)

# Display output scores
print("Output Scores :", output.detach())

# Display predicted class
print("Predicted Class :", output.argmax().item())
