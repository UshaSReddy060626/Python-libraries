import numpy as np
marks=np.array([56,89,78,55,34,21,89])
print(np.sum(marks))
print(np.mean(marks))
print(np.median(marks))
print(np.min(marks))
print(np.max(marks))
print(np.argmin(marks))
print(np.argmax(marks))
print(np.std(marks))
print(np.var(marks))
print(np.unique(marks))

#sorting
print(np.sort(marks))

#argsort
print(np.argsort(marks))

#reshaping arrays
arr=np.arange(12)
print(arr.reshape(3,4))

#flatten
matrix=np.array([[1,2],[3,4]])
print(matrix.flatten())

#ravel
print(matrix.ravel())

#transpose
print(matrix.transpose())

#resize
a1=np.array([1,2,3,4])
a1.resize((2,2))
print(a1)

#squeeze
print(a1.squeeze())

#expand_dims
b=np.array([1,2,3])
print(np.expand_dims(b,axis=0))

#joining arrays
a=np.array([23,45])
b=np.array([45,78])
print(np.concatenate((a,b)))

#vstack
print(np.vstack(a))

#hstack
print(np.hstack(b))

#stack
print(np.stack(a))

#splitting arrays
a2=np.array([[23,56],[78,67]])
print(np.split(a2,2))

#hsplit
print(np.hsplit(a2,2))

#vsplit
print(np.vsplit(a2,2))

#random module
np.random.seed(10)
a=np.random.rand(2,3)
print(a)

#randn()
print(np.random.randn(2,3))

#randint()
print(np.random.randint(1,10,size=5))

#choice
color=["red","blue","green","pink","yellow"]
print(np.random.choice(color))

#shuffle
np.random.shuffle(color)
print(color)

#permutation
np.random.permutation(color)
print(color)

#dot
prices = np.array([10, 20, 30])
quantity = np.array([2, 1, 3])
print(np.dot(prices, quantity))

#matmul() and @
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print(np.matmul(A, B))
print(A @ B)

#transpose
print(A.T)

#inverse
print(np.linalg.inv(A))

#determinant
print(np.linalg.det(A))

#eigenvalues
value,vector=np.linalg.eig(A)
print(A)

#vectorization
num=np.array([1,2,3,4])
result=num*2
print(result)

#copy vs view
arr = np.array([1,2,3])
view = arr.view()
copy = arr.copy()
arr[0] = 100
print(view)
print(copy)

#shallow vs deep copy
original = np.array([1, 2, 3])
shallow = original.view()
shallow[0] = 99
deep = original.copy()
deep[1] = 88
print(original)  
print(shallow)   
print(deep)      
