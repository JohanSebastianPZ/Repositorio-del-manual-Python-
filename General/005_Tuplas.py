"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 005_Tuplas.py
============================================================================
"""

# trabajando con tuplas
# son como listas pero de piedra inmutables

# formas de empezar una tupla desde cero
mi_tupla = tuple()  # usando el constructor oficial
otra_tupla = ()     # el clasico atajo con parentesis

print(type(mi_tupla))
print(type(otra_tupla))

# guardamos mis datos en una tupla
mi_tupla = (22, 1.65, "sebastian", "martinez")
print(mi_tupla)
print(type(mi_tupla))

# acceso a los datos
# buscamos por posicion empezando siempre desde el 0
print(mi_tupla[0])   # el primer dato 22
print(mi_tupla[-1])  # el ultimo de la fila martinez

# ojo si pides un indice que no existe python se queja
# print(mi_tupla[4])   # error te pasaste de largo
# print(mi_tupla[-6])  # error no hay tantos elementos hacia atras

# herramientas utiles
# cuantas veces aparece este valor
print(mi_tupla.count("sebastian"))

# en que posicion esta ana su primer match
print(mi_tupla.index("sebastian"))
print(mi_tupla.index("martinez"))

# el corazon de las tuplas la inmutabilidad
# intentar cambiar un dato asi nomas no funcionara
# mi_tupla[1] = 1.70  # esto lanzara un error porque la tupla no se toca
# print(mi_tupla)

# lo que si podemos hacer es sumar tuplas para crear una nueva
otra_tupla = ("estudiante", "python", "ilerna")
tupla_sumada = mi_tupla + otra_tupla
print(tupla_sumada)

# el truco para editarlas
# si de verdad necesitas cambiar algo conviertela en lista primero
mi_tupla = list(mi_tupla)
print(type(mi_tupla))  # magia ahora es una lista

# ahora que es lista ya no hay restricciones
mi_tupla[0] = 23                 # actualizo la edad
mi_tupla.insert(1, "barcelona")  # añado la ciudad donde vivo
print(mi_tupla)

# cuando termines los cambios la devuelves a su estado original tupla
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))  # bloqueada de nuevo

# borrado
# no puedes borrar un solo elemento por la inmutabilidad
# del mi_tupla[2]  # esto falla

# pero puedes borrar la variable entera de la memoria
# del mi_tupla
# print(mi_tupla)  # dara error porque la variable simplemente ya no existe