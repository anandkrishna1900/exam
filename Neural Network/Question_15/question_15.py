# Question 15: Analyze dimensionality reduction effects.

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch
import torch.nn as nn

# Define a 4 x 4 input feature map
feature_map = torch.tensor([[[[1, 2, 3, 4],
                              [5, 6, 7, 8],
                              [9, 10, 11, 12],
                              [13, 14, 15, 16]]]],
                            dtype=torch.float32)

# Display dimensions of the input feature map
print("Input Shape :", feature_map.shape)

# Create a Max Pooling layer with a 2 x 2 window
max_pool = nn.MaxPool2d(kernel_size=2)

# Apply Max Pooling
output = max_pool(feature_map)

# Display dimensions of the output feature map
print("Output Shape:", output.shape)

# Display the pooled output
print("\nOutput Feature Map:\n", output.squeeze())
