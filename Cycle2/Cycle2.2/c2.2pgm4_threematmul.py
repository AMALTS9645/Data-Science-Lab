import numpy as np
#matrix multiplication of 3 matrices.
arr1=np.arange(1,10).reshape((3,3))
arr2=np.arange(11,20).reshape((3,3))
arr3=np.arange(21,30).reshape((3,3))
print("\n1stmatrix")
print(arr1)
print("\n2ndmatrix")
print(arr2)
print("\n3rdmatrix")
print(arr3)
a=np.multiply(arr1,arr2)
b=np.multiply(a,arr3)
print("\nThe product of 3 matrices:")
print(b)