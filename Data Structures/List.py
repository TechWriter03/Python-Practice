ls=[]

ls.append(1)
ls.insert(1,2)
ls.append(3)
ls.extend([6,5,4])
ls.append(3)
print(ls)
print(ls.count(3))

ls.pop()
ls.pop(0)
ls.remove(6)
print(ls)

ls.sort()
print(ls)

ls.reverse()
print(ls)
