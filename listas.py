#crear una lista
lista = ['Numpy',"Pandas", "TensorFlow, Keras"]
number = [1,2,3, 4]
print (lista)
print(type(number))
mix = ["Alex", 1.65, True, [2,3,4]]
print(mix)
print(len(mix))
print("primer elemento de la lista: ", mix[0])
print("ultimo elemento de la lista: ", mix[-1])
string = "Numpy"
print("primera letra de la lista: ", string[0])
print("ultima letra de la lista: ", string[-1])
print(mix[0:2])
print(mix[2:])
mix.append("Santiago")
print(mix)
mix.insert(0, "Alex")
print(mix)
print("el numero mayor de la lista es: ", max(number))
print("el numero menor de la lista es: ", min(number))

del number[-1]
print(number)

del number[0:2]
print(number)