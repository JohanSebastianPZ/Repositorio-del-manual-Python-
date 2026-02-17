"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 001_Variables.py
============================================================================
"""

# CONSULTAR EL TIPO DE DATO

print(type('Hola Python')) # tipo de dato str
print(type(5)) # tipo int
print(type(2.3)) # tipo float
print(type(True)) # tipo boolean
print(type(3 + 3)) # tipo complex

# VARIABLES EN PYTHON

my_string_variable = 'my string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_float_variable = 3.14
print(my_float_variable)

# Asi imprimo varios datos
print(my_int_variable, my_bool_variable, my_float_variable)

# FUNCION STR: CONVERSION DE DATOS

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))  

print(my_string_variable, str(my_int_variable), my_bool_variable)

# VARIABLES EN UNA SOLA LINEA

name, surname, alias, age = 'sebastian', 'martinez', 'La maquina del chambeo', 25
print('me llamo', name, surname, ' Mi edad es: ', age, ' y mi alias es: ', alias)

# CAMBIO DE TIPO DE DATO

name = 34
age = 'sebas'

print(name)
print(age)

# FORZAMOS EL TIPO

addrees = str('mi direccion')
address = str("mi direccion")
print(type(address))

address = 32
print(type(address))

address = True
print(type(address))

address = 2.2
print(type(address))

# EJEMPLOS CON MIS DATOS PERSONALES

my_name = 'sebastian'
my_surname = 'martinez'
my_age = 25
my_alias = 'La maquina del chambeo'

print(f"Mi nombre es {my_name} {my_surname} y mi edad es {my_age} y mi alias es {my_alias}")

