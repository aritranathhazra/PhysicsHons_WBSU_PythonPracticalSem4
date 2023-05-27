import numpy as np

# Input number of equations
R = int(input("Enter the number of equations: "))

# Input coefficient matrix
print("Enter the coefficients equation-wise:")
a = np.zeros((R, R))
for i in range(R):
    for j in range(R):
        a[i, j] = float(input(f"Enter the value of a{i+1}{j+1}: "))

# Input constant values
print("Enter the r.h.s constant numbers equation-wise:")
b = np.zeros(R)
for i in range(R):
    b[i] = float(input(f"Enter the value of b{i+1}: "))

# Calculate determinant of coefficient matrix
det = np.linalg.det(a)
print("Determinant of the coefficient matrix =", det)

# Solve the system of equations
augmented_matrix = np.hstack((a, b.reshape(R, 1)))
solutions = np.linalg.solve(a, b)
print("Solutions of the unknown variables are:")
for i, solution in enumerate(solutions):
    print("X", i+1, "=", solution)

# Calculate inverse of coefficient matrix
inverse = np.linalg.inv(a)
print("The inverse of the coefficient matrix:")
print(inverse)
