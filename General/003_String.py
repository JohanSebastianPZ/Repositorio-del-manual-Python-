"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 003_String.py
============================================================================
"""

# defino variables de texto
my_string = "My String"
my_othher_string = "Mi otro String"

# Los caracteres se cuenta en la funcion len()
print(len(my_string))
print(len(my_othher_string))

# Concatenacion de cadenas
print(my_string + my_othher_string)

# Aqui se agrega espacio al momento de hacer la concatenacion
print(my_string + " - " + my_othher_string)

# Caracteres especiales
my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

# \t = tabulacion
my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

# Si quieto mostrar la \ uso doble \\
my_new_line_string = "\\tEste es un String\\ncon salto de linea"
print(my_new_line_string)

# Formateo: insertar valores en texto
name, surname, age = "Sebastian", "Martinez", 25
print("Mi nombres es" + name + " " + surname  + " y mi edad es " + str(age))

# s = String
# f = Float
# d = entero

# Esta es la version con %
print("Mi nombre es %s %s y mi edad es %s, prueba %d" % (name, surname, age,(2000 - 2025)))

# Esta es la version con {}
print("Mi nombre es {} {} y mi edad es {}, prueba {}".format(name, surname, age, (2000 - 2025)))

numero =  432.43214234321423
print(f"Mi nombre es {name} {surname} y mi edad es {type(numero)}")

# Desempaquetado de datos
language = "Python"

a,b,c,d,e,f = language

print(a)
print(e)

# Division de cadenas
print('Division')

language = "Python"

# toma desde la posicion 1 hasta la posicion 2 (esto inicia desde el 0 )
language_slice = language[1:3]
print(language_slice)

# toma  desde la posicion 1 hasta el final
language_slice = language[1:]
print(language_slice)

# toma los ultimos 2 caracteres
language_slice = language[-2:]

# Reverse: invierte la cadena
reversed_language = language[::-1]
print(reversed_language)

# Funciones de Strings

print(language.capitalize()) # 1. Primera letra en mayúscula
print(language.upper()) # 2. Todo en mayúsculas
print(language.count("t")) # 3. Cuenta cuántas veces aparece "'"
print(language.isnumeric()) # 4. Verifica si todos los caracteres son numéricos
print("1".isnumeric()) # 5. Ejemplo: True porque "1" es un número
print(language.lower()) # 6. Todo en minúsculas
print(language.upper().isupper()) # 7. Comprueba si está en mayúsculas 
print(language.startswith("py")) # 8. Este método verifica si la cadena almacenada en la variable language no empieza con el texto "py"