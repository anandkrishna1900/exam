# Question 19: Generate synthetic images using a GAN in PyTorch.

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# Generator Network
# nn.Sequential() arranges layers one after another
generator = nn.Sequential(
    # Fully connected layer: 100 random values -> 128 features
    nn.Linear(100, 128),
    # Add non-linearity
    nn.ReLU(),
    # Fully connected layer: 128 features -> 784 pixel values
    nn.Linear(128, 784),
    # Restrict pixel values between 0 and 1
    nn.Sigmoid()
)

# Discriminator Network
# Determines whether an image is real or generated
discriminator = nn.Sequential(
    # Fully connected layer: 784 pixel values -> 128 features
    nn.Linear(784, 128),
    # Add non-linearity
    nn.ReLU(),
    # Fully connected layer: 128 features -> 1 real/fake score
    nn.Linear(128, 1),
    # Restrict score between 0 and 1
    nn.Sigmoid()
)

# Create random noise
# Noise is used as input to the Generator
noise = torch.randn(1, 100)

# Generate a synthetic image from noise
fake_image = generator(noise)

# Check whether the generated image appears real or fake
score = discriminator(fake_image)

# Reshape output into a 28 x 28 image
fake_image = fake_image.view(28, 28)

# Display the generated image
plt.imshow(fake_image.detach().numpy(), cmap="gray")
plt.title("Generated Image")
plt.show()

# Display image dimensions
print("Generated Image Shape :", fake_image.shape)

# Display discriminator score
print("Real/Fake Score :", score.item())
