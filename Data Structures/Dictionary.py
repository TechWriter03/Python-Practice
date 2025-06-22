d={}

d['a']=1
d['b']=2
print(d)

print(d['a'])
print(d.get('b'))
print(d.get('c',0))

print(d.keys())
print(d.values())
print(d.items())

d.pop('b')
print(d)
