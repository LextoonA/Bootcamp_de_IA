import numpy as np

#Creación de un ndarray 2D

matriz = np.array ([[1,2,3], [4,5,6]])
#Acceso a un elemento especifico de la matriz

elemento= matriz [1,2]
print (elemento)

#Selección de la fila 0

fila = matriz [0, :]
print (fila)

#Selección de columna 1

columna= matriz [: , 1]
print (columna)
