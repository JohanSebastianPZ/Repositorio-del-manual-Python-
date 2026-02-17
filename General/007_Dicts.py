"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 007_Dicts.py
=============
"""

# dicts o diccionarios guardan info con parejas de clave y valor
# la clave es como la etiqueta para encontrar el dato rápido

# formas de crear un diccionario
mi_dict = dict()  # usando el constructor oficial
print(type(mi_dict))  # clase dict

mi_otro_dict = {}  # con llaves vacías también funciona
print(type(mi_otro_dict))  # clase dict


# me monto un diccionario con mis cosas
mi_otro_dict = {
    "nombre": "sebastian",
    "apellido": "martinez",
    "edad": 22,
    1: "python"  # las claves pueden ser números si quieres
}


# un diccionario puede tener de todo hasta un set dentro
mi_dict = {
    "nombre": "sebastian",
    "apellido": "martinez",
    "edad": 22,
    "lenguajes": {"python", "swift", "kotlin"},  # aquí el valor es un set
    "1": "algun python"
}

print(mi_otro_dict)
print(mi_dict)


# para saber cuántas claves tiene metidas
print(len(mi_otro_dict))  # cuenta las etiquetas no los datos sueltos
print(len(mi_dict))

# entrar a un valor usando su etiqueta es lo mejor que tienen
print(mi_dict["nombre"])

# cambiar un dato es tan fácil como asignarle uno nuevo a la misma clave
mi_dict["nombre"] = "pedro"
print(mi_dict["nombre"])

# meter una clave nueva con su valor sobre la marcha
mi_dict["calle"] = "calle nou"
print(mi_dict)

# si te has equivocado y quieres borrar una clave usa del
del mi_dict["calle"]
print(mi_dict)

# el buscador in solo mira en las claves no en los valores
print("sebastian" in mi_dict)  # sale false porque sebastian es el dato no la etiqueta
print("nombre" in mi_dict)  # sale true porque nombre sí es una clave

# trucos para sacar info limpia
print(mi_dict.items())    # saca las parejas clave valor juntas
print(mi_dict.keys())     # saca solo la lista de etiquetas
print(mi_dict.values())   # saca solo los datos guardados


# crear diccionarios nuevos de forma rápida con fromkeys
# crea uno nuevo con estas claves pero sin valores están vacíos
mi_nuevo_dict = mi_otro_dict.fromkeys(("nombre", 1))
print(mi_nuevo_dict)

# va genial para resetear un diccionario manteniendo las etiquetas
mi_nuevo_dict = dict.fromkeys(mi_dict)
print(mi_nuevo_dict)

# o para crear uno donde todas las claves empiecen con el mismo valor
mi_nuevo_dict = dict.fromkeys(mi_dict, "sebastian")
print(mi_nuevo_dict)
