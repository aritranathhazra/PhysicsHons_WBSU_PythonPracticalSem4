import numpy as np

R = int(input("Enter the number of equations:"))

print("Enter the coefficients equationwise:")
a = np.array([[float(input()) for _ in range(R)] for _ in range(R)])
p = np.copy(a)

print("Enter the r.h.s constant numbers equationwise: ")
b = np.array([float(input()) for _ in range(R)])

det = np.linalg.det(p)
print("Determinant of coefficient matrix =", det)

sol = np.linalg.solve(a, b)

print("Solution of the equations:")
for i, x in enumerate(sol):
    print(f"X{i} =", x)
