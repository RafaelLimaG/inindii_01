import numpy as np

#declarar as matrizes
a = np.array([[1,1],[-3,1]])
b = np.array([[6],[2]])

x = np.linalg.solve(a,b)
print(x)