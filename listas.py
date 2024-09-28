lista= ["NumPy", 
        "Pandas",
        "Scikit-learn",
        "TensorFlow",
        "Keras"]
print(lista)

numbers = [1, 2, 3, 4, 5] 
print(numbers)
print(type(numbers))
print("Mayor: ", max(numbers)) #solo funciona con datos de tipo entero
print("Menor:", min(numbers)) #solo funciona con datos de tipo entero
print(numbers)
del numbers[-1] #borra el último elemento de la lista
#del numbers -- así podemos borrar la lista completa pero al momento de imprimirla saldría error
print(numbers)

string="NumPy"
print("Primer elemento: ", string[0])
print("Segundo elemento: ", string[0])
print("Último elemento: ", string[0])

mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(len(mix))
print("Se imprimirá el primer elemento que es el: ", mix[0])
print("Se imprimirá el segundo elemento que es el: ", mix[1])
print("Se imprimirá el último elemento que es el: ", mix[-1])
print(mix[0:2])
print(mix[:2]) #Se puede omitir el 0 
print(mix[2:]) #Así le decimos que imprima desde la posición 2 en adelante
print(mix[2:-2]) #Así le decimos que imprima desde x posición a x posición 
mix.append(["Romulo", "Nancy"]) #con .apped agregamos elementos a la lista
mix.insert(0, "Jheyson Galvis")
print(mix)
