# Question 9: Perform 2D Convolution operation on an Image using PyTorch.

import torch

image = torch.tensor([[1, 2, 3, 0, 1],
                      [4, 5, 6, 1, 2],
                      [7, 8, 9, 2, 3],
                      [1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 0]], dtype=torch.float32)

image = image.unsqueeze(0).unsqueeze(0)

kernel = torch.tensor([[ 1,  0, -1],
                       [ 1,  0, -1],
                       [ 1,  0, -1]], dtype=torch.float32)

kernel = kernel.unsqueeze(0).unsqueeze(0)

output = torch.nn.functional.conv2d(image, kernel)

print("Input Image:\n", image.squeeze())
print("\nKernel:\n", kernel.squeeze())
print("\nConvolution Output:\n", output.squeeze())
