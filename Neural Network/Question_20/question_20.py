# Question 20: K-means clustering algorithm.

import torch
import matplotlib.pyplot as plt

# Data
data = [
    [25, 79], [34, 51], [22, 53], [27, 78], [33, 59], [33, 74], [31, 73],
    [22, 57], [35, 69], [34, 75], [67, 51], [54, 32], [57, 40], [43, 47],
    [50, 53], [57, 36], [59, 35], [52, 58], [65, 59], [47, 50], [49, 25],
    [48, 20], [35, 14], [33, 12], [44, 20], [45, 5],  [38, 29], [43, 27],
    [51, 8],  [46, 7]
]

X = torch.tensor(data, dtype=torch.float32)

# Number of clusters
k = 3

# Initialize centroids randomly
indices = torch.randperm(X.size(0))[:k]
centroids = X[indices]

# K-Means iterations
for _ in range(100):
    # Compute distances between each point and centroid
    distances = torch.cdist(X, centroids)
    # Assign points to nearest centroid
    labels = torch.argmin(distances, dim=1)
    
    # Compute new centroids
    new_centroids = torch.stack([
        X[labels == i].mean(dim=0)
        for i in range(k)
    ])
    
    # Check convergence
    if torch.allclose(centroids, new_centroids, atol=1e-4):
        break
        
    centroids = new_centroids

print("Centroids:")
print(centroids)

# Convert to NumPy for plotting
X_np = X.numpy()
labels_np = labels.numpy()
centroids_np = centroids.numpy()

# Plot clusters
plt.scatter(X_np[:, 0], X_np[:, 1], c=labels_np, s=50, alpha=0.5)
plt.scatter(centroids_np[:, 0], centroids_np[:, 1], c='red', s=200, marker='X')
plt.xlabel("x")
plt.ylabel("y")
plt.title("K-Means Clustering using PyTorch")
plt.show()

print("\nOutput Centroids:")
print(centroids)
