import numpy as np

#Suma de elementos

arr = np.array ([1,2,3])
print (np.sum(arr))

array = np.array ([[1,2,3], [4,5,6]])
print ("Array original: ")
print (array)

reshape_array = array.reshape (3,2)
print ("Array reshapel: ")
print (reshape_array)

flatten_array= array.flatten ()
print("Array flatten: ")
print(flatten_array)

trasnpose_array = array.transpose ()
print("Array transpose: ")
print(trasnpose_array)
