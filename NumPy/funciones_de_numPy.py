import numpy as np

#Creación de un ndArray con valores del 0 al 9 sin incluir el 10

numeros1= np.arange (0,10)
print (numeros1)

#Creación de un ndArray con valores de 2en 2 del 1 al 10

numeros2 = np.arange (0,11,2)
print (numeros2)

#Creación de un ndArray con valores del 0 al 4 sin incluir el 4 de 0.5 en 0.5

numeros3= np.arange (0,4, 0.5)
print(numeros3)

#Creación de ndArray con 10 valores espaceados uniformemente entre 0 y 1

puntos1= np.linspace (0, 1, 10)
print (puntos1)

#Creación de ndArray con 5 valores espaceados uniformemente entre 2 y 10

puntos2= np.linspace (2, 10, 5)
print (puntos2)

#Creando matriz aleatoria

matriz_aleatoria = np.random.rand (3,3)
print (matriz_aleatoria)

#Cración de matriz aleatoria de 5 elementos

vector_aleatorio = np.random.rand (5)
print (vector_aleatorio)