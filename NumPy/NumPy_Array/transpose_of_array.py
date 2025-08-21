import numpy as np

array = np.random.randint(0,10,(2,3))
print(array)
print(array.shape)

trans = np.transpose(array)
print(trans)
print(trans.shape)
#or 
trans2 = array.T 
print(trans2)
print(trans2.shape)