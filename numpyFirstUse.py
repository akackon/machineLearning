import numpy as np
from math import sin
x = np.array([1,2,3], dtype = np.float32)
print(x)
print(str(type(x)))
print(x.itemsize)
print([sin(i) for i in [1,2,3]])