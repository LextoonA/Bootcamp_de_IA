import numpy as np

numeros_aleatorios_uniformes = np.random.rand (3)
print ("Números aleatorios uniformes: ")
print (numeros_aleatorios_uniformes)

numeros_aleatorios_enteros = np.random.randint (1, 10, size=5)
print ("Numeros aleatorios enteros: ")
print (numeros_aleatorios_enteros)

numeros_aleatorios_normales = np.random.randn (2,2)
print ("Números aleatorios normales: ")
print (numeros_aleatorios_normales)

arr1 = np.array ((1,2,3))
arr2 = np.array ([4,5,6])

#Suma de elementos de los arreglos
result = arr1 + arr2
print ("El resultado de la suma de matrices es: ", result)

#Producto por una constante en este caso el 2
arr = np.array ((1,2,3))
result = 2 * arr
print ("El resultado del producto es: ", result)

#Suma de matrices

arr3 = np.array ([[1,2], [3,4]])
arr4 = np.array ([[5,6], [7,8]])
result = arr3 + arr4
print ("El resultado de la suma de matrices es: ", result)

#

arr5 = np.array ([[1,2,3,4,5,6]])
reshape_arr = arr5.reshape (2,3)
print ("La matriz con reshape sería: ")
print (reshape_arr)
total_sum = arr5.sum ()
print ("La suma de los elementos de la matriz es: ")
print (total_sum)

#mean calcula la media de los elementos de la matriz 
arr6 = np.array ([(1,2,3), [4,5,6]])
averange = arr6.mean ()
print (averange)

#Para el máximo y minimo usamo max y min
valor_max = arr6.max ()
print ("El valor máximo de la matriz es: ")
print (valor_max)
valor_min = arr6.min ()
print ("El valor mínimo de la matriz es: ")
print (valor_min)

#Para conocer la posición de los valores max y min usamos 

arr7 = np.array ([3,5,7,8,1])
idx_min = arr7.argmin ()
print ("La posición del valor minimo es: ")
print (idx_min)
idx_max = arr7.argmax ()
print ("La posición del valor máximo es: ")
print (idx_max)

#Desviación estandar

arr8 = np.array ([1,2,3,4,5,6])
desviacion = arr.std ()
print ("La pdesviación es: ")
print (desviacion)
