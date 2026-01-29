# Write a Python Program to implement K-Means Clustering on numpy random dataset. 

import numpy as np
import matplotlib.pyplot as plt


def kmeans(X, k, max_iters=100, tol=1e-4):
    """
    K-means clustering algorithm.

    Parameters:
    - X: Input data (numpy array)
    - k: Number of clusters
    - max_iters: Maximum number of iterations
    - tol: Tolerance to declare convergence

    Returns:
    - centroids: Final centroids of clusters
    - clusters: Index of the cluster each data point belongs to
    """

    # Initialize centroids randomly
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]

    for _ in range(max_iters):
        # Assign each data point to the nearest centroid
        distances = np.linalg.norm(
            X - centroids[:, np.newaxis],
            axis=2
        )
        clusters = np.argmin(distances, axis=0)

        # Update centroids
        new_centroids = np.array([
            X[clusters == j].mean(axis=0)
            for j in range(k)
        ])

        # Check for convergence
        if np.linalg.norm(new_centroids - centroids) < tol:
            break

        centroids = new_centroids

    return centroids, clusters


# Generate some random data for testing
np.random.seed(42)
X = np.concatenate([
    np.random.normal(loc=i, scale=0.5, size=(50, 2))
    for i in range(4)
])

# Apply K-means clustering
k = 4
centroids, clusters = kmeans(X, k)

# Plot the results
plt.figure(figsize=(8, 6))

for i in range(k):
    plt.scatter(
        X[clusters == i, 0],
        X[clusters == i, 1],
        label=f'Cluster {i + 1}'
    )

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker='X',
    color='black',
    s=200,
    label='Centroids'
)

plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

