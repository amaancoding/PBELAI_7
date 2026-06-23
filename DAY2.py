#list
my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))

#prop. and method
print(len(my_list))
my_list.append(6)
print(my_list)

my_list.insert(0,11)
print(my_list)

my_list.extend([7,8,9])
print(my_list)

my_list.remove(3)
print(my_list)

my_list.pop()
print(my_list)

#properties
#ordered
my_list[7]=10
print(my_list)
#duplicasy and heterogeneity
FUN = [1,2,3,4,5,12,True,False,"Hello"]
print(FUN)
print(type(FUN))

##tuple
abc=(1,2,3,4,5)
print(abc)
print(type(abc))

#set
my_set= {1,2,3,4,5}
print(my_set)
print(type(my_set))

#dictionary
my_dict = {"name":"John", "age":30, "city":"New York"}
print(my_dict)
print(type(my_dict))

#string
my_string = "Hello, World!"
print(my_string)
print(type(my_string))