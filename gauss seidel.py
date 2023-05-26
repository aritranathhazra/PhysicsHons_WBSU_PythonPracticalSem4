import numpy as np
# User inputs
n = int(input("Enter the number of equations: "))
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"Enter the coefficient a{i+1}{j+1}: "))
B = np.zeros(n)
for i in range(n):
    B[i] = float(input(f"Enter the constant b{i+1}: "))
# Initializing variables
X = np.zeros(n)
itr = 0
err = 1000
# Iteration loop
while err > 1.e-06:
    itr += 1
    X0 = X.copy()
    for i in range(n):
        s = np.dot(A[i, :], X) - A[i, i]*X[i]
        X[i] = (B[i] - s) / A[i, i]
    err = np.linalg.norm(X - X0)
# Printing results
print("Solution vector:")
print(X)
print("Number of iterations:", itr)