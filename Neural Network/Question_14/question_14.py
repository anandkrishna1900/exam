# Question 14: Compare max pooling and average pooling using PyTorch.

import torch
import torch.nn as nn

# Define a 4 x 4 input feature map
feature_map = torch.tensor([[[[1, 2, 3, 4],
                              [5, 6, 7, 8],
                              [9, 10, 11, 12],
                              [13, 14, 15, 16]]]],
                            dtype=torch.float32)

# Create a Max Pooling layer with a 2 x 2 window
max_pool = nn.MaxPool2d(kernel_size=2)
# Apply Max Pooling
max_output = max_pool(feature_map)

# Create an Average Pooling layer with a 2 x 2 window
avg_pool = nn.AvgPool2d(kernel_size=2)
# Apply Average Pooling
avg_output = avg_pool(feature_map)

# Display the input feature map
print("Input Feature Map:\n", feature_map.squeeze())

# Display the output of Max Pooling
print("\nMax Pooling Output:\n", max_output.squeeze())

# Display the output of Average Pooling
print("\nAverage Pooling Output:\n", avg_output.squeeze())
