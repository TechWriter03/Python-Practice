# LIST
my_list = [1,2,"santhosh",3]

my_list.append(5)
my_list.insert(4,4)
print(my_list)

my_list.pop()
my_list.pop(-1)
my_list.remove("santhosh")
print(my_list)

print(my_list[::-1])
print(my_list[-3:])
print(my_list[::2])

# List Comprehenion (return loop condition)
new_list = [i*i for i in my_list if (i!=1)]
print(new_list)
print()

# DICTIONARY
my_dict = {'a':1,'b':2,'c':3}
my_dict['a'] = 10
my_dict.pop('c')
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print()

# SET
a = {1,2,4}
a.add(3)
a.remove(4)
print(a)
b = {3,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

a = {}
print(type(a))

a = set()
print(type(a))