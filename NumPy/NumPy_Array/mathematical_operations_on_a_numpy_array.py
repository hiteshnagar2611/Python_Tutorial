import numpy as np

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

print(list1+list2)


a = np.random.randint(0,10,(3,3))
b = np.random.randint(10,20,(3,3))

print(a)
print(b)

print(a+b)   #or print(np.add(a,b))
print(a-b)   #or print(np.subtract(a,b))
print(a*b)   #or print(np.multiply(a,b))
print(a/b)   #or print(np.divide(a,b))
