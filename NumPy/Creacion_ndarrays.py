import numpy as np

#Lista de números
numeros = [1,2,3,4,5]
#Creación de NdArray a partir de la lista 
NdArray_numeros = np.array (numeros)
print (NdArray_numeros)

#Creando Ndarray con dimensiones 
#Creación de Ndarray de 2x3 con ceros

matriz_ceros = np.zeros ((2,3))

#Creación de Ndarray de 3x3 con unos

matriz_unos = np.ones ((3,3))

#Creación matriz personalizada 

matriz_personalizada = np.array ([[1,2,3] , [4,5,6]])

print (matriz_ceros)
print (matriz_unos)
print (matriz_personalizada)
