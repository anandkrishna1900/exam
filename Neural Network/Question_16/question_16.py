# Question 16: Load a pre-trained CNN model. Perform feature extraction using the model. Fine-tune the model for a custom dataset.

import torch
import torch.nn as nn
from torchvision import models

# Load pre-trained ResNet18 model
model = models.resnet18(weights='DEFAULT')

# Freeze all layers for feature extraction
for param in model.parameters():
    param.requires_grad = False

# Replace the original 1000-class output layer with a 5-class output layer
model.fc = nn.Linear(model.fc.in_features, 5)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()

# Calculate prediction error / Train only final layer
optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

# Create sample images and labels
images = torch.randn(4, 3, 224, 224)  # 4 RGB images
labels = torch.tensor([0, 1, 2, 3])     # Class labels

# Fine-tune the model for 3 epochs
for epoch in range(3):
    output = model(images)                       # Generate predictions
    loss = criterion(output, labels)             # Compute loss
    optimizer.zero_grad()                        # Clear old gradients
    loss.backward()                              # Compute gradients
    optimizer.step()                             # Update weights

# Test the model using a sample image
test_image = torch.randn(1, 3, 224, 224)
with torch.no_grad():
    result = model(test_image)

# Display output shape
print("Output Shape :", result.shape)

# argmax() returns the index of the highest score
print("Predicted Class :", result.argmax().item())
