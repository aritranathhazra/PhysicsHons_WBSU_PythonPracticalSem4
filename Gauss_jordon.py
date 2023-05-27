import numpy as np

# Input number of equations
R = int(input("Enter the number of equations:"))

# Input coefficient matrix
print("Enter the coefficients equationwise:")
a = np.array([[float(input()) for i in range(R)] for j in range(R)], dtype=float)

# Input constant values
print("Enter the r.h.s constant numbers equationwise:")
b = np.array([float(input()) for i in range(R)], dtype=float)

# Calculate determinant of coefficient matrix
det = np.linalg.det(a)
print("Determinant of the coefficient matrix =", det)

# Solve the system of equations
augmented_matrix = np.hstack((a, b.reshape(R, 1)))
solutions = np.linalg.solve(a, b)
print("Solutions of the unknown variables are:")
for i, solution in enumerate(solutions):
    print("X", i, "=", solution)

# Calculate inverse of coefficient matrix
inverse = np.linalg.inv(a)
print("The inverse of coefficient matrix:")
print(inverse)
