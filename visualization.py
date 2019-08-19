import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100,500,50,)
y = np.random.randint(100,1000,50,)

print(x)
print(y)

plt.scatter(x,y, marker = "^",color = "red")
plt.scatter(y,x, marker = "^",color = "green")
plt.title("This is a sample scatter plot")
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.show()