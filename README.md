# EIGENVALUES-AND-EIGENVECTORS
## Aim:
To write a python program to find the Eigenvalues and Eigen Vectors
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
Step 1:

Import the required library NumPy using import numpy as np.

Step 2:

Define or input the square matrix for which eigenvalues and eigenvectors are to be calculated.

Step 3:

Use the built-in function np.linalg.eig() to compute the eigenvalues and eigenvectors of the given matrix.
(This function returns two results: eigenvalues and eigenvectors.)

Step 4:

Display the eigenvalues and eigenvectors as the output.
## Program:
```
#Program to find the eigen values and eigen vectors.
#Developed by: Kabilan S
#RegisterNumber: 212225230119
import numpy as np

A = np.array([[2, 2],
              [1, 3]])

w, v = np.linalg.eig(A)

print("Eigen values are", w, "and Eigen Vectors are", v)
```
## Output:
<img width="1920" height="1080" alt="Screenshot 2026-02-10 112936" src="https://github.com/user-attachments/assets/c14e480e-8a3f-4e03-9896-d2b61146bb89" />


## Result:
Thus the Eigenvalue and Eigenvector is successfully solved using python program
