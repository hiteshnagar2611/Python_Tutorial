import numpy as np

a = np.random.randint(0,10,(2,3))
print(a)
print(a.shape)

b = a.reshape(3,2)
print(b)
print(b.shape)