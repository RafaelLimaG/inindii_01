import numpy as np
from numpy.linalg import solve as ls


T1 = 273.15
T2 = 298.15
T3 = 373.15

R1 = 35563
R2 = 10000
R3 = 549.4

R = [np.log(R1), np.log(R2), np.log(R3)]
Rc = [np.power(np.log(R1),3), np.power(np.log(R2),3), np.power(np.log(R3),3)]
#declarar as matrizes
x = np.array([1, 1, 1] , R , Rc)
y = np.array([[(1/T1)],[(1/T2)],[(1/T3)]])
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



# resultado = ls(x,y)
# print(resultado)