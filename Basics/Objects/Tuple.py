#once you create a element in tuple you can not change it

tuple_1 = (2,3,4,5)
print(tuple_1)

#tuples allows multiple data types
tuple_2 = (1,2,3.4,'machine',True)
print(tuple_2)

#converting a list to a tuple
my_list = [1,2,3,4]
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[2])

#tuples are immutable
#my_type.append(6)  # throw error 

#size of tuple
print(len(my_tuple))