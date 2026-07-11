# 1-D Array
import numpy as np
a=np.array([1,2,3])
print(a)


# 2-D Array
b=np.array([[2,3.4,6],[7,8,9]])
print(b)

#3-D Array
c=np.array([[[3,5],[6,9]]])
print(c)

#dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)

#shape
print(a.shape)
print(b.shape)
print(c.shape)

#size
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

#type
print(a.dtype)
print(b.dtype)
print(c.dtype)

#nbytes
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)

#acess specific elements
num=np.array([[23,4,56,78,90,10],[87,65,23,56,21,12]])
print(num[1,3])
print(num[0,-2])

#get a specific row
print(num[0,:])

#get a specific column
print(num[:,2])

#step size
print(num[1,3:5:1])

#change elements
num[0,2]=13
print(num)

#creating arrays
number=np.zeros((2,3))
print(number)
print(number.ndim)

#ones
number=np.ones((3,2,4))
print(number)
print(number.ndim)

#full
number=np.full((3,3),12)
print(number)

#full_like
print(np.full_like(a,16))

#random
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))

#random integer
print(np.random.randint(-1,3,size=(2,3)))

#identity
print(np.identity(3))

#repeat
arr=np.array([[23,45,67,89]])
r1=np.repeat(arr,2,axis=1)
print(r1)

#arange
arr=np.arange(1,11)
print(arr)

#step-size
print(np.arange(0,5,2))

#linspace
print(np.linspace(0,11,5))

#eye
print(np.eye(2))

#convert array type
arr=arr.astype(float)
print(arr)

#reverse
print(arr[::-1])

#boolean indexing
marks=np.array([50,60,70,80])
print(marks>50)
print(marks[marks>50])

#where
result=np.where(marks>50,"pass","fail")
print(result)

#array operations
nums=np.array([23,56,7])
print(arr+10)
print(arr-10)
print(arr*10)
print(arr/2)
print(arr//2)
print(arr**2)
print(arr%2)

#broadcasting
arr=np.array([[23,56,78],[6,7,8]])
print(arr+10)

#universal functions
a1=np.array([4,7,5])
print(np.sqrt(a1))
print(np.abs(a1))
print(np.exp(a1))
print(np.log(4))
print(np.sin(7))
print(np.cos(0))


