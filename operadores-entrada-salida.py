nombre = input("ingrese tu nombre");
print(nombre);

edad = input("ingrese tu edad");
print(edad)
#imprimer el tipo
#print(type(edad))

apodo = input("Cómo te dicen tus amigos");
comida = input("¿Cual es tu comida favorita?");
color = input("¿Cual es tu color favorito?");
anime = input("¿Cual es tu anime favorito?");
pelicula = input("¿Cual es tu pelicula favorita?");
gebero_musical = input("¿Cual es tu genero musical favorito?");
actor1 = input("¿Cual es tu primer actor favorito?");
actor2 = input("¿Cual es tu segundo actor favorito?");
actor3 = input("¿Cual es tu tercer actor favorito?");
#lista de actores
actores = [actor1, actor2, actor3]
sueño = input("¿Cual es tu sueño?");
bebida_fria = input("¿Cual es tu bebida favorita para quitar el calor?");
bebida_caliente = input("¿Cual es tu bebida favorita para quitar el frio?");
superpoder = input("¿Cual es tu superpoder favorito?");

print("Hola " + nombre + " te dicen " + apodo + " tienes " + edad + " años, tu comida favorita es " + comida + " tu color favorito es " + color + " tu anime favorito es " + anime + " tu pelicula favorita es " + pelicula + " tu genero musical favorito es " + gebero_musical + " tus actores favoritos son " + actores[0] + ", " + actores[1] + " y " + actores[2] + " tu sueño es " + sueño + " tu bebida favorita para quitar el calor es " + bebida_fria + " tu bebida favorita para quitar el frio es " + bebida_caliente + " tu superpoder favorito es " + superpoder);