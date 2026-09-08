# Question 12: Compute output dimensions of a convolution layer for different strides and padding values using PyTorch.

import torch
import torch.nn as nn

# Create a 32 x 32 grayscale image with random values
# Shape format: (batch_size, channels, height, width)
image = torch.randn(1, 1, 32, 32)

# Create a convolution layer with:
# 1 input channel, 1 output channel,
# 3 x 3 kernel, stride = 1, padding = 0
conv1 = nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=0)
# Apply convolution to the input image
output1 = conv1(image)

# Display output dimensions
print("Stride = 1, Padding = 0")
print("Output Shape:", output1.shape)

# Create a convolution layer with stride = 2 and padding = 0
conv2 = nn.Conv2d(1, 1, kernel_size=3, stride=2, padding=0)
# Apply convolution to the input image
output2 = conv2(image)

# Display output dimensions
print("\nStride = 2, Padding = 0")
print("Output Shape:", output2.shape)

# Create a convolution layer with stride = 1 and padding = 1
conv3 = nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=1)
# Apply convolution to the input image
output3 = conv3(image)

# Display output dimensions
print("\nStride = 1, Padding = 1")
print("Output Shape:", output3.shape)

# Create a convolution layer with stride = 2 and padding = 1
conv4 = nn.Conv2d(1, 1, kernel_size=3, stride=2, padding=1)
# Apply convolution to the input image
output4 = conv4(image)

# Display output dimensions
print("\nStride = 2, Padding = 1")
print("Output Shape:", output4.shape)
