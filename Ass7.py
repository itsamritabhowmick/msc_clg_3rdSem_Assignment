import numpy as np
import matplotlib.pyplot as plt

# -------------------- DATA --------------------

X = np.array([
    [1590, 2.9], [1540, 2.7], [1600, 2.6], [1590, 2.7], [1520, 2.5],
    [1540, 2.4], [1560, 2.3], [1490, 2.3], [1510, 2.4], [1350, 3.9],
    [1360, 3.7], [1370, 3.8], [1380, 3.7], [1410, 3.6], [1420, 3.9],
    [1430, 3.4], [1450, 3.7], [1460, 3.2], [1590, 3.9], [1540, 3.7],
    [1600, 3.6], [1490, 3.7], [1520, 3.5], [1540, 3.4], [1560, 3.3],
    [1460, 3.3], [1510, 3.4], [1340, 2.9], [1360, 2.4], [1320, 2.5],
    [1380, 2.6], [1400, 2.1], [1320, 2.5], [1310, 2.7], [1410, 2.1],
    [1305, 2.5], [1460, 2.7], [1500, 2.9], [1300, 3.5], [1320, 3.6],
    [1400, 2.7], [1300, 3.1], [1350, 3.1], [1360, 2.9], [1305, 3.9],
    [1430, 3.0], [1440, 2.3], [1440, 2.5], [1380, 2.1], [1430, 2.1],
    [1400, 2.5], [1420, 2.3], [1310, 2.1], [1350, 2.0]
])

Y = np.array([
    'accepted','accepted','accepted','accepted','accepted',
    'accepted','accepted','accepted','accepted','accepted',
    'accepted','accepted','accepted','accepted','accepted',
    'accepted','accepted','accepted','accepted','accepted',
    'accepted','accepted','accepted','accepted','accepted',
    'accepted','accepted',
    'rejected','rejected','rejected','rejected','rejected',
    'rejected','rejected','rejected','rejected','rejected',
    'rejected','rejected','rejected','rejected','rejected',
    'rejected','rejected','rejected','rejected','rejected',
    'rejected','rejected','rejected','rejected','rejected',
    'rejected','rejected','rejected'
])

# 🔧 FIX: align labels with features
Y = Y[:len(X)]

# -------------------- TRAIN-TEST SPLIT --------------------

def train_test_split(X, Y, test_size=0.2, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)

    indices = np.arange(len(X))
    np.random.shuffle(indices)

    split = int((1 - test_size) * len(X))
    train_idx, test_idx = indices[:split], indices[split:]

    return X[train_idx], X[test_idx], Y[train_idx], Y[test_idx]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# -------------------- KNN --------------------

def knn_predict(X_train, Y_train, x, k):
    distances = np.linalg.norm(X_train - x, axis=1)
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = Y_train[nearest_indices]

    labels, counts = np.unique(nearest_labels, return_counts=True)
    return labels[np.argmax(counts)]

# -------------------- PREDICTION & ACCURACY --------------------

predictions = [knn_predict(X_train, Y_train, x, k=3) for x in X_test]
accuracy = np.mean(predictions == Y_test)

print(f"Accuracy: {accuracy * 100:.2f}%")

# -------------------- VISUALIZATION --------------------

plt.figure(figsize=(10, 6))
plt.scatter(X[Y == 'accepted'][:, 0], X[Y == 'accepted'][:, 1],
            color='green', label='Accepted')
plt.scatter(X[Y == 'rejected'][:, 0], X[Y == 'rejected'][:, 1],
            color='red', label='Rejected')

# Decision Boundary
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h)
)

Z = np.array([
    knn_predict(X_train, Y_train, [x, y], k=3)
    for x, y in np.c_[xx.ravel(), yy.ravel()]
])

Z = Z.reshape(xx.shape)
Z = np.where(Z == 'accepted', 1, 0)

plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.3)

plt.xlabel("SAT Score")
plt.ylabel("GPA")
plt.title("KNN Classification (Custom Implementation)")
plt.legend()
print(plt.show())

