#initial values 

import numpy as np

#create a numpy array of 0's
x = np.zeros((4,5))
print(x)

#create a numpy array of 1's
y = np.ones((2,2))
print(y)

# create a numpy array of a perticular value
z = np.full((3,3),4)
print(z)

# create a identical metrix
a = np.eye(4)
print(a)

#create a numpy array with randome values
b = np.random.random((3,4))
print(b)

#create a numpy array with random integer value within specific range
c = np.random.randint(10,100,(3,4))
print(c)

#array of evenly spaced values 
d = np.linspace(10,30,5)
print(d)

#array of evenly spaced values 
e = np.arange(20,40,4)
print(e)