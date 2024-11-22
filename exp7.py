import numpy as num
# 0-D array
arr = num.array(32)
print(arr)
# 1-D array
ar1 = num.array([23, 32, 38])
print(ar1)
# 3-D array
ar2 = num.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(ar2)
# linear algebra
# Dot
ar1 = num.array([10, 20, 21])
ar2 = num.array([23, 32, 38])
result = num.dot(ar1, ar2)
print(result)
# vDot
ar1 = num.array([[10, 2], [3, 4]])
ar2 = num.array([[5, 63], [72, 8]])
result = num.vdot(ar1, ar2)
print(result)
# inner
ar1 = num.array([[10, 2], [3, 4]])
ar2 = num.array([[5, 63], [72, 8]])
result = num.inner(ar1, ar2)
print(result)
# multiplication
ar1 = num.array([[1, 2], [3, 4]])
ar2 = num.array([[5, 6], [7, 8]])
print(f"multiplication of matrix is:{num.matmul(ar1, ar2)}")
# determinant
ar1 = num.array([[1, 5], [6, 4]])
print(f"Determinant is:{num.linalg.det(ar1)}")
# solve for x and y
ar1 = num.array([[1, 2], [3, 4]])
ar2 = num.array([10, 11])
print(f"X and Y are : {num.linalg.solve(ar1, ar2)}")
# inverse
ar1 = num.array([[1, 2], [3, 4]])
print(f"inverse is:{num.linalg.inv(ar1)}")
