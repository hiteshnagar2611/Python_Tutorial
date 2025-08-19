#list should be included in square brackets
#stores multiple values
#list are mutable 
#list allows duplicate values

my_list = [1,2,3,4,5]
print(my_list)

#list can multiple data types
my_list1 =[1,2.2,"hello",True]
print(my_list1)

#Add element to a list 
my_list1.append(4)
print(my_list1)

#print elements of list using index
print(my_list1[1])
print(my_list1[2])

#list allows duplicate values
my_list3 = [1,2,3,3,4,4]
print(my_list3)

#size of list 
print(len(my_list3))

#delete an item in list
list_1 = [1,2,1.3,"hello",True]
del list_1[3]
print(list_1)

#Join Two lists
list_3 = [1,2,3,4,5]
list_4 = [6,7,8,9,10]
list_5 = list_3 + list_4
print(list_5)