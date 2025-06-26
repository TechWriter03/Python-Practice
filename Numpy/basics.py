import numpy as np

arr=np.array([[10,20],[30,40],[50,60]],dtype=float)
print(arr)

print(arr.ndim)
print(arr.size)
print(arr.shape)

a=np.zeros((2,3))
print(a)

b=np.arange(1,5)
print(b)

arr=arr.reshape(2,3)
print(arr)

print(arr.ravel())

print(arr.min())
print(arr.max())
print(arr.sum())
print(arr.sum(axis=1))
print(arr.sum(axis=0))

print(np.sqrt(arr))
print(np.std(arr))

c=np.array([[1,2],[3,4]])
d=np.array([[5,6],[7,8]])

print(c+d)
print(c*d)

print(c.dot(d))
