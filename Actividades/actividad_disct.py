my_dict = {
    "nombre": "Geral",
    "Apellido": "Lopez",
    "Edad": 35,
    "Languajes": {"Python", "Ingles", "Castellano"},
}

print(my_dict["nombre"])

del my_dict["Apellido"]

print(my_dict)

# Esto es para eliminar todo el diccionario
# del my_dict

print('nombre' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# Esto es util cuando creamos un nuevo diccionario pero usando todas las claves del diccionario original
my_new_dict = my_dict.fromkeys(('nombre', 1))
print(my_new_dict)

my_new_dict = my_dict.fromkeys((my_dict, 'Geral'))
print(my_new_dict)

