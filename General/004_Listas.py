"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 004_Listas.py
============================================================================
"""

# Listas

my_list = list() # Aqui creo una lista usando el constructor de la lista
my_other_list = [] # Esta es la forma mas utilizada

# Aqui se cuantos elementos tiene la lista
print(len(my_list))

my_list = [1, 2, 3, 4, 5, 6, 7]
print(my_list)
print(len(my_list))

# Listas con distintos tipos de datos
my_other_list = [35, 1.60, 'Sebastian', 'Martinez']

print(len(my_other_list))

print(type(my_other_list))

# Acceso a los elementos de la lista usando el indice
print(my_other_list[1])
print(my_other_list[-1])

# Metodo count(): cuenta cuantas veces aparece un valor
print(my_other_list.count('Sebastian'))
print(my_other_list.count(35))

prueba = "Esto es una prueba"

# Desempaquetado de Listas
age, height, name, surname, prueba = my_other_list

# Desempaquetado cambiando el orden
age, height, name, surname, prueba = my_other_list[2], my_other_list[1]
print(my_other_list)

# Concatenacion de listas
print(my_list + my_other_list)

my_list = list('Hola Python')

print(my_list)

# metodo .append(): agrega elemento al final
my_other_list.append("ilerna")
print(my_other_list)

# metodo insert(): inserta elemento en una posicion especifica
my_other_list.insert(1, "Azul")
print(my_other_list)

# las listas son mutables (se pueden modificar)
my_other_list[1] = "Rojo"
print(my_other_list)

# metodo remove(): elimina el objeto que espcifiquemos
my_other_list.remove(35)
print(my_other_list)

# metodo pop(): eleimina elemento por posicion
print(my_list.pop()) #Elimina el ultimo elemento
print(my_list)

print(my_list.pop(2))
print(my_list)

# operador del: elimina elemento por posicion
del my_list[2]
print(my_list)

# metodo clear(): vacia la lista completa
my_list.clear()
print(my_list)

# metodo copy(): crea una copia de la lista
mi_nueva_list = my_list.copy()

print(mi_nueva_list)

# metodo sort(): ordena los elementos de menos a mayor o por oden alfabetico en el caso de letras
mi_nueva_list.sort()
print(mi_nueva_list)

