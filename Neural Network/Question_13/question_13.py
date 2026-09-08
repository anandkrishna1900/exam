# Question 13: Design a simple CNN architecture for image classification using PyTorch.

import torch
import torch.nn as nn

# Create a CNN model using Sequential
model = nn.Sequential(
    # Extract features from the input image using 8 filters
    nn.Conv2d(1, 8, kernel_size=3),
    # Introduce non-linearity into the network
    nn.ReLU(),
    # Reduce the size of feature maps and retain important features
    nn.MaxPool2d(kernel_size=2),
    # Convert feature maps into a one-dimensional vector
    nn.Flatten(),
    # Classify the image into one of 10 classes
    nn.Linear(8 * 13 * 13, 10)
)

# Display the CNN architecture
print(model)

# Create a sample grayscale image of size 28 x 28
# Shape format: (batch_size, channels, height, width)
dummy_input = torch.randn(1, 1, 28, 28)

# Pass the image through the CNN model
output = model(dummy_input)

# Display the dimensions of the input image
print("\nInput Shape :", dummy_input.shape)

# Display the dimensions of the output
print("Output Shape:", output.shape)

# Remove gradient information and display output scores for 10 classes
print("Output (Class Scores):", output.detach())
