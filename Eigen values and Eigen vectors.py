#Program to find the eigen values and eigen vectors.
#Developed by: Kabilan S
#RegisterNumber: 212225230119
import numpy as np

A = np.array([[2, 2],
              [1, 3]])

w, v = np.linalg.eig(A)

print("Eigen values are", w, "and Eigen Vectors are", v)
