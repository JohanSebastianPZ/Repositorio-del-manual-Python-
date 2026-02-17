
#Parte 1 – Datos personales

#1. Crea tres variables para guardar:
#o Tu nombre completo (tipo str)
#o Tu edad (tipo int)
#o Si eres estudiante o no (tipo bool)
nombre = "johan sebastian neiva martinez"
edad = 25
estudiante = False
#2. Muestra la información en pantalla con frases personalizadas.
print("Hola" , nombre)
print("Tienes " , edad , " años")
print("y tu estado como estudiante es: " , estudiante)
#3. Usa la función type() para mostrar el tipo de dato de cada variable.
print(type(nombre))
print(type(edad))
print(type(estudiante))
#4. Cambia el valor de una de las variables y muestra nuevamente elresultado.
nombre = "Johan"
print("Tu nuevo nombre es: " , nombre)

#------------------------------------------------------------------------------------------------------------

#Parte 2 – Gustos personales

#Pide al usuario tres cosas que le gusten (por ejemplo: leer, música, viajar).
color = input("Ingrese un color:")
animal = input("Ingrese un animal:")
pais = input("Ingrese un pais:")
#2. Guarda esas respuestas en una lista llamada gustos.
gustos = [color, animal, pais]
#3. Muestra la lista completa en pantalla.
print(gustos)
#4. Usa la función len() para mostrar cuántos elementos tiene la lista.
print("Longitud del array: ", len(gustos))
#5. Crea una nueva lista llamada gustos_modificados que repita los gustos dos veces (usando gustos * 2).
gustos_modificados = gustos * 2
print(gustos_modificados)
#6. Muestra el resultado y explica en un comentario qué observas.
# Se muestra los items del array repetidos, la cantidad de veces especificadas, en este caso 2

#------------------------------------------------------------------------------------------------------------

# Parte 3 – Comidas favoritas
#1. Crea una tupla llamada comidas_favoritas con tres comidas que te gusten mucho.
comidas_favoritas = ("salchipapa", "arroz", "salmon")
# 2. Muestra la tupla completa.
print(comidas_favoritas)
# 3. Intenta cambiar uno de los valores de la tupla (solo como experimento).o Escribe en un comentario qué sucede y por qué.
#comidas_favoritas[1] = "atun" # - Esto muestra un arroz porque no se pueden editar las tuplas
print(comidas_favoritas[1])
# 4. Usa len() para contar cuántas comidas hay en la tupla.
print(len(comidas_favoritas))

#------------------------------------------------------------------------------------------------------------

# Parte 4 – Conjunto de números
# 1. Crea un conjunto (set) llamado numeros con algunos números repetidos, por ejemplo:
# 2. numeros = {1, 2, 2, 3, 4, 4, 5}
numeros = {1, 2, 2, 3, 4, 4, 5}
# 3. Muestra el conjunto en pantalla y observa qué sucede con los valores duplicados.
print(numeros)
# 4. Agrega otro número al conjunto reescribiendo la variable, por ejemplo:
# 5. numeros = numeros | {6}
numeros = numeros | {4}
# 6. Muestra nuevamente el conjunto y observa el cambio.
print(numeros)
# 7. Escribe un comentario explicando por qué los valores repetidos no aparecen más de una vez.
# Un conjunto, a diferencia de una tupla, no acepta duplicados y sí se puede modificar; mientras que una tupla acepta duplicados pero no se puede cambiar.

#------------------------------------------------------------------------------------------------------------

# Parte 5 – Tipos de datos y resumen
# 1. Usa la función type() para mostrar el tipo de dato de:
# o Tu variable nombre
# o La lista gustos
# o La tupla comidas_favoritas
# o El conjunto numeros

print(nombre)
print(gustos)
print(comidas_favoritas)
print(numeros)

# 2. Crea una nueva lista llamada resumen que contenga las tres estructuras principales:
# 3. resumen = [gustos, comidas_favoritas, numeros]
# 4. Muestra el contenido de resumen y comenta qué observas al combinar diferentes tipos de datos en una lista.

resumen = [gustos, comidas_favoritas, numeros]

print(resumen)

# El resultado muestra un array con otros array dentro
# [['verde', 'gato', 'colombia'], ('salchipapa', 'arroz', 'salmon'), {1, 2, 3, 4, 5}]

#------------------------------------------------------------------------------------------------------------

# Parte 6 – Reto de lógica
# 1. Usa la edad que guardaste en la parte 1.
# 2. Escribe un bloque de código que imprima un mensaje diferente según la edad:
    # o Si la edad es menor de 18: muestra “Eres menor de edad”.
    # o Si la edad es entre 18 y 30: muestra “Eres joven”.
    # o Si es mayor de 30: muestra “Eres adulto”.
# 3. Usa operadores lógicos (and, or) para combinar condiciones.
# 4. Explica en un comentario qué hace tu código y por qué.

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 30:
    print("Eres joven")
else:
    print("Eres adulto")

#------------------------------------------------------------------------------------------------------------

#Parte 7 – Reflexiona
# Responde en tu documento:
# 1. ¿Qué tipo de dato devuelve la función input()?
    # La funcion input() pide ingreso de datos
# 2. ¿Por qué el conjunto no muestra los valores duplicados?
    # Un conjunto no acepta valores duplicados ni tiene un orden
# 3. ¿Cuál es la diferencia entre una lista y una tupla?
    # La diferencia es que la lista si es modificable y la tupla no
# 4. ¿Qué sucede si cambias el orden de los elementos en un conjunto?
    # nada, porque los conjuntos no tienen un orden indefinido
# 5. ¿Por qué las listas permiten modificaciones y las tuplas no?
    # Las listas permiten modificaciones porque son estructuras de datos mutables, en cambio las tuplas no son
    # estructuras de datos mutables
# 6. ¿Qué ventajas tiene usar conjuntos en un programa?
    # Los conjuntos si permiten modificaciones.
# 7. En el bloque de lógica, ¿por qué crees que se usan condiciones en orden (if, elif, else) y no todas a la vez?
    # Las condiciones if, elif o else se usan evaluar condiciones una por una.