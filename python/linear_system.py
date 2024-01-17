import numpy as np
from numpy.linalg import solve as ls

T1 = 0
T2 = 25
T3 = 100

# Conversão Kelvin para Celsius
vetTemp = np.array([[(T1 + 273.15)],[(T2 + 273.15)],[(T3 + 273.15)]])

R1 = 35563
R2 = 10000
R3 = 549.4

R = np.log([R1, R2, R3])
Rc = np.power(np.log([R1, R2, R3]), 3)

# Declarar as matrizes
x = np.array([[1, R[0], Rc[0]], [1, R[1], Rc[1]], [1, R[2], Rc[2]]])
y = 1/vetTemp
print(y)
print(R)
print(Rc)

"""
[x + y] = [6]
[-3x + y] = [2]

[A + B * ln(R) + C * ln(R)^3 = 1/T]
[A + B * ln(R) + C * ln(R)^3 = 1/T]
[A + B * ln(R) + C * ln(R)^3 = 1/T]

"""

resultado = ls(x,y)
print(resultado)