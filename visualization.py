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
# plt.show()
# Commenting the above line because it makes the running of the code below long to get to

# Working with bar plots now
x = np.arange(5)
y = np.random.randint(50,100,5)

print(x)
print(y)
# xlist = list("ABCDE")
xlist = ["English", "Math", "History", "Science", "Geography"]
plt.title("Marks scored by John")
plt.xticks(x,xlist)
plt.bar(x,y)
plt.show()