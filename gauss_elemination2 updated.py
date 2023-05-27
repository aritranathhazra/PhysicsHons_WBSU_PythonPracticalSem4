import numpy as np

R = int(input("Enter the number of equations: "))

print("Enter the coefficients equation-wise:")
a = np.array([[float(input(f"a{i+1}{j+1}: ")) for j in range(R)] for i in range(R)])
p = np.copy(a)

print("Enter the r.h.s constant numbers equation-wise:")
b = np.array([float(input(f"b{i+1}: ")) for i in range(R)])

det = np.linalg.det(p)
print("Determinant of the coefficient matrix =", det)

sol = np.linalg.solve(a, b)

print("Solution of the equations:")
for i, x in enumerate(sol):
    print(f"X{i+1} =", x)
