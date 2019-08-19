import pandas as pd
import numpy as np

data = np.array([[1,2,3], [3,4,5], [4,5,6]])
df = pd.DataFrame(data)
df.columns = list('ABC')

print(df['A'])

def foo(x):
    return(x**2)
    
print(foo(4))
print(df.shape)
print(df['C'].apply(foo))
print(df['C'])