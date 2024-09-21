#Operadores numericos

a=10
b=3
print("suma:", a+b)
print("Resta:", a-b)
print("Multiplicación:",a*b)
print("División:",a/b)

#En Python se usa el signo % para obtener el residuo de la división

print("Modulo:",a%b)

#En Python como en matemáticas dividir entre 0 es un error 

#División entera
print("División entera:",a//b)

#Potenciación
print("Potencia:",a**b)

#Para sumarle n valor a la variable a se podría poner a= a+n o mejor:

a += 2 
print(a)

#PEMDAS
operacion_1 = 2+3*4
operacion_2 = 2 + (3*4)
operacion_3 = (2+3) * (4**2) / 8-1

print(operacion_1)
print(operacion_2)
print(operacion_3)

#comparaciones 
print (a<b)
print (a>b)
print (a>=b)
print(a<=b)
print(a==b)
print(a!=b)

