#Listas

lista= ["Alex Arcos", "Licenciado en informática", True, 1.65]
print(lista) #en el mundo de la programación se inicia a contar desde el 0
print(lista[0])
lista[0] = "Alexander Granja Arcos" #se modifica un elemento de la lista
print(lista[0])

#Tupla -- No se puede modificar este tipo de lista

tupla= ("Café", "huevos", "pan", "manzana", True, 8.50)
print(tupla[1])
#tupla[3] = "naranja" muestra un error porque las tuplas no se pueden modificar

#Conjuntos - set en inglés

conjunto = {"Alex Arcos", "Licenciado en informática", True, 1.65, "licenciado en informática"}
print(conjunto) #no imprime datos duplicados
#Creando un enunciado
print(f"El conjunto es: {conjunto}") 

#Creación de diccionario - su estructura es clave: valor

diccionario ={
    "Nombre" : "Alex",
    "Apellido" : "Granja",
    "Edad": 34,
    "Profesion" : "Docente",
    "Está feliz" : True
}
print(diccionario)
print(diccionario["Nombre"])
print(diccionario["Apellido"])
print(diccionario["Edad"])