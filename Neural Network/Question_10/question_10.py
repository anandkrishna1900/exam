# Question 10: Apply edge detection, blur and sharpen filters to an image using PyTorch.

import torch

image = torch.tensor([[1, 2, 3, 0, 1],
                      [4, 5, 6, 1, 2],
                      [7, 8, 9, 2, 3],
                      [1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 0]], dtype=torch.float32)

image = image.unsqueeze(0).unsqueeze(0)

edge_filter = torch.tensor([[ 1,  0, -1],
                            [ 1,  0, -1],
                            [ 1,  0, -1]], dtype=torch.float32)

blur_filter = torch.tensor([[1/9, 1/9, 1/9],
                            [1/9, 1/9, 1/9],
                            [1/9, 1/9, 1/9]], dtype=torch.float32)

sharpen_filter = torch.tensor([[ 0, -1,  0],
                               [-1,  5, -1],
                               [ 0, -1,  0]], dtype=torch.float32)

edge_filter = edge_filter.unsqueeze(0).unsqueeze(0)
blur_filter = blur_filter.unsqueeze(0).unsqueeze(0)
sharpen_filter = sharpen_filter.unsqueeze(0).unsqueeze(0)

edge_output = torch.nn.functional.conv2d(image, edge_filter)
blur_output = torch.nn.functional.conv2d(image, blur_filter)
sharpen_output = torch.nn.functional.conv2d(image, sharpen_filter)

print("Input Image:\n", image.squeeze())
print("\nEdge Detection Output:\n", edge_output.squeeze())
print("\nBlur Output:\n", blur_output.squeeze())
print("\nSharpen Output:\n", sharpen_output.squeeze())
