"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 008_Condicionales.py
============================================================================
"""

# empezamos con lo mas basico un booleano directo
my_condition = True
if my_condition:
    # si es true entra aqui de cabeza
    print("se ejecuta la condiicon if")
print("la ejecucion continua")

# ahora probamos con una operacion matematica
my_condition = 5 * 2

if my_condition == 10:
    # como 5 por 2 es 10 esta condicion se cumple
    print("se ejecuta la condicion del segundo if")

# aqui decidimos que camino tomar si se cumple o no
if my_condition > 10:
    print("es mayor que 10")
else: 
    # si la condicion de arriba falla caemos en este saco
    print("es menor o igual que 10")
    
print("la ejecucion continua")

# metemos logica doble con and para que sea mas especifico
if my_condition > 10 and my_condition < 20:
    # solo entra si cumple las dos cosas a la vez
    print("es mayor que 10 y menor que 20")
else:
    # si falla cualquiera de las dos venimos aqui
    print("es menor o igual que 10 o mayor o igual que 10")

print("la ejecucion continua")

# usamos elif para mirar varias opciones antes de rendirnos al else
if my_condition > 10 and my_condition < 20:
    print("es mayor que 10 y menor que 20")
elif my_condition == 1:
    # si la primera no fue pero es igual a 1 entra aqui
    print("es igual a 1")
else:
    # si no ha entrado en ninguna de las anteriores termina aqui
    print("es menor o igual que 10 o mayor o igual que 20")

print("la ejecucion continua")

# ojo con los strings vacios que python los ve como algo falso
my_string = ""
if not my_string:
    # si el string no tiene nada el not lo convierte en true y entra
    print("mi cadena de texto es vacia")

my_string = "mi cadena de texto"

# corregido para que el flujo tenga sentido con lo anterior
if my_string:
    # ahora que tiene texto se considera que existe y es true
    print("mi cadena de texto es valida")

if not my_string:
    # esto no se vera porque el string ahora si tiene contenido
    print("esto no saldra por pantalla")
