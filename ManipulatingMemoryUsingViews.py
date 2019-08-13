from numpy.lib.stride_tricks import as_strided
import numpy as np
x = np.arange(16)
y = as_strided(x,(7,4),(8,4))
print(y)