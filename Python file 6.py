import numpy as np
array1=np.array([1,2,3])
print('array1 type:',type(array1))
print('array1 array 형태:',array1.shape)

array2 = np.array([[1,2,3],
                  [2,3,4]])
print('array2 type:', type(array2))
print('array2 array 형태:', array2.shape)

array3=np.array([[1,2,3,]])
print('array3 type:', type(array3))
print('array3 array 형태:', array3.shape)

a1=np.array([1,2,3,4,5])
print(a1)
print(type(a1))
print(a1.shape)
print(a1[0],a1[1],a1[2],a1[3],a1[4])


a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
               [[1,2,3],[4,5,6],[7,8,9]],
               [[1,2,3],[4,5,6],[7,8,9]]])
print(a3)
print(a3.shape)