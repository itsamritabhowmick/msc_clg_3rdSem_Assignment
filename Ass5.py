# Write a Python Program to solve Travelling Salesman Problem using Branch and Bound, to find optimal path with minimum cost 

import numpy as np
import matplotlib.pyplot as plt

# Data
X = np.array([
    32.50234527, 53.42680403, 61.53035803, 47.47563963, 59.81320787,
    55.14218841, 52.21179669, 39.29956669, 48.10504169, 52.55001444,
    45.41973014, 54.35163488, 44.1640495, 58.16847072, 56.72720806,
    48.95588857, 44.68719623, 60.29732685, 45.61864377, 38.81681754
])

Y = np.array([
    31.70700585, 68.77759598, 62.5623823, 71.54663223, 87.23092513,
    78.21151827, 79.64197305, 59.17148932, 75.3312423, 71.30087989,
    55.16567715, 82.47884676, 62.00892325, 75.39287043, 81.43619216,
    60.72360244, 82.89250373, 97.37989686, 48.84715332, 56.87721319
])

# Hyperparameters
learning_rate = 0.0001
num_iterations = 1000

# Initialize parameters (slope and intercept)
m = 0   # slope
b = 0   # intercept

# Lists to store history for plotting
cost_history = []
weight_history = []

# Gradient Descent
for iteration in range(num_iterations):
    # Predicted values
    Y_pred = m * X + b

    # Compute cost (Mean Squared Error)
    cost = np.mean((Y_pred - Y) ** 2)
    cost_history.append(cost)
    weight_history.append(m)

    # Compute gradients
    dm = (-2 / len(X)) * np.sum(X * (Y - Y_pred))
    db = (-2 / len(X)) * np.sum(Y - Y_pred)

    # Update parameters
    m -= learning_rate * dm
    b -= learning_rate * db

# Plot the data and the fitted line
plt.scatter(X, Y, label='Data points')
plt.plot(X, m * X + b, color='red', label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Plot cost vs weight graph
plt.scatter(weight_history, cost_history, label='Data points', color='blue', marker='o')
plt.plot(weight_history, cost_history, label='Cost vs. Weight', color='red')
plt.xlabel('Weight (Slope)')
plt.ylabel('Cost')
plt.title('Cost vs. Weight with Data Points')
plt.legend()
plt.show()

print(f"Final Slope (m): {m}")
print(f"Final Intercept (b): {b}")

