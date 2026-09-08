# Question 21: Apply PCA for a sample dataset and classify.

from sklearn.datasets import load_iris
import torch

# Load Iris dataset
iris = load_iris()
X = torch.tensor(iris.data, dtype=torch.float32)

# Mean-center the data
X_centered = X - X.mean(dim=0)

# Covariance matrix
cov_matrix = torch.cov(X_centered.T)

# Eigen decomposition
eigenvalues, eigenvectors = torch.linalg.eigh(cov_matrix)

# Sort eigenvalues and eigenvectors in descending order
idx = torch.argsort(eigenvalues, descending=True)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Select first 2 principal components
k = 2
principal_components = eigenvectors[:, :k]

# Project data onto principal components
X_pca = X_centered @ principal_components

# Print results
print("Eigenvalues:")
print(eigenvalues)
print("\nPrincipal Components:")
print(principal_components)
print("First Principal Component (PC1):")
print(principal_components[:, 0])
print("Second Principal Component (PC2):")
print(principal_components[:, 1])
print("\nTransformed Data (first 5 samples):")
print(X_pca[:5])
print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
