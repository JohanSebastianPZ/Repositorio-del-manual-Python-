"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 006_Sets.py
============================================================================
"""

# sets o conjuntos no tienen orden y pasan de los duplicados

# formas de crear un set
mi_set = set()  # usando el constructor oficial
mi_otro_set = {}  # ojo que esto crea un diccionario no un set

print(type(mi_set))        
print(type(mi_otro_set))  

# para que sea un set con datos hay que usar llaves
mi_otro_set = {"ana", "martinez", 22}
print(type(mi_otro_set))  # ahora sí es un set de verdad

# para ver cuántas cosas hay dentro
print(len(mi_otro_set))

# añadir cosas con add
mi_otro_set.add("ana")
print(mi_otro_set)  # si ya estaba no hace nada porque no repite

# los sets pasan de los repetidos olímpicamente
mi_otro_set = {"ana", "martinez", 22, "ana"}  # puse ana dos veces
print(type(mi_otro_set))
mi_otro_set.add("ana")
print(mi_otro_set)  # solo guarda una ana y ya está

# usar in para ver si algo está dentro es super rápido en sets
print("ana" in mi_otro_set)        
print("martiness" in mi_otro_set)  

# quitar cosas con remove
mi_otro_set = {"python", "ana", "developer"}
mi_otro_set.remove("ana")
print(mi_otro_set)

# vaciarlo todo con clear
mi_otro_set.clear()
print(mi_otro_set)  # se queda el set pelado

# borrar la variable de la faz de la tierra
mi_otro_set = {"python", "ana", "developer"}
del mi_otro_set
# print(mi_otro_set)  # explota porque ya no existe

# si necesitas orden pásalo a lista
mi_set = {"ana", "martinez", 22}
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[0])  # en lista sí puedo usar índices

# unir conjuntos con union
mi_set = {"ana", "martinez", 22}
mi_otro_set = {"java", "php", "python"}
mi_nuevo_set = mi_set.union(mi_otro_set)
print(mi_nuevo_set)  # junta todo y limpia duplicados solo

# ver qué tiene uno que no tenga el otro
print(mi_nuevo_set.difference(mi_set))

# ver qué cosas tienen en común
print(mi_set.intersection(mi_otro_set))
