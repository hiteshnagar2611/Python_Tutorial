import numpy as np
from time import process_time

#time taken by a list
python_list = [i for i in range(10000000)]
start_time = process_time()
python_list = [i+5 for i in python_list]
end_time = process_time()
print(end_time - start_time)

#time taken by a NumPy Array
np_array = np.array([i for i in range(10000000)])
start_time1 = process_time()
np_array +=5
end_time1 = process_time()
print(end_time1 - start_time1)