"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 009_Loops.py
============================================================================
"""

# loops o bucles sirven para repetir codigo y no escribir lo mismo mil veces

# el while repite todo mientras la condicion sea verdad
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2  # importante ir sumando para que no sea infinito

print("==============================================================")

# el while tambien puede llevar un else cuando termina el ciclo
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    # esto sale justo cuando la condicion de arriba deja de cumplirse
    print("mi condicion es mayor o igual que 10")
print("la ejecucion continua...")

print("==============================================================")

# ojo que esto no es un while else son dos cosas sueltas
# primero hace todo el bucle y luego mira el if de abajo
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2

if my_condition == 10:
    print("mi condicion es igual a 10")
else:
    print("mi condicion es mayor que 10")

print("la ejecucion continua...")

print("==============================================================")

# podemos meter un if dentro para chequear cosas en cada vuelta
my_condition = 0
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("mi condicion es 15")
print(my_condition)

print("==============================================================")

# el break es para romper el bucle y salir corriendo
my_condition = 10
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene la ejecucion")
        break  # corta el bucle aqui mismo y sale
print(my_condition)
print("la ejecucion continua...")

# el for es para ir elemento por elemento en una lista o coleccion
print("==============================================================")

# recorriendo una lista de numeros
my_list = [35, 24, 62, 52, 30, 0, 17]
for element in my_list:
    print(element)

print("==============================================================")

# tambien funciona con sets pero recuerda que no tienen orden
my_set = {"ana", "martinez", 22}
for element in my_set:
    print(element)

print("==============================================================")

# en las tuplas tambien va sacando cada dato uno por uno
my_tuple = (22, 1.65, "ana", "martinez", "barcelona")
for element in my_tuple:
    print(element)

print("==============================================================")

# en los diccionarios por defecto solo te saca las claves
my_dict = {"Nombre": "ana", "Apellido": "martinez", "Edad": 22, 1: "python"}
for element in my_dict:
    print(element)

print("==============================================================")

# si quieres los datos usa values para sacar los valores
for element in my_dict.values():
    print(element)
else:
    print("el bucle for para diccionario ha finalizado")

print("==============================================================")

# el continue lo que hace es saltarse lo que queda de esa vuelta
for element in my_dict:
    print(element)
    if element == "Edad":
        continue  # deja de leer lo de abajo y vuelve arriba al siguiente giro
    print("despues del continue")
else:
    print("el bucle for para diccionario ha finalizado")

print("==============================================================")

# otro ejemplo para que se vea que se salta el print si coincide
for element in my_dict:
    if element == "Edad":
        continue  # salta a la siguiente iteracion sin imprimir edad
    print(element)
else:
    print("el bucle for para diccionario ha finalizado")

print("\n=== fin de la leccion de bucles ===")