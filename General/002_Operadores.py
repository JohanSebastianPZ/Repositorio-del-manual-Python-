"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 002_Operadores.py
============================================================================
"""

# Operaciones Basicas
print("Suma:", 3 + 4)
print("Resta:", 3 - 4)
print("Multiplicación:", 3 * 4)
print("División:", 3 / 4)

# Operadores Modulo
print("Módulo 3 % 4:", 3 % 4)
print("Módulo 10 % 3:", 10 % 3)

# Operadores Division entera
print("División entera 10 // 3:", 10 // 3)

# Operadores Potencia
print("Potencia 2 ** 3:", 2 ** 3)

# Concatenacion texto

# Esto me lo mostrara sin el espacio
print("hola" + "python")

# Esto me lo mostrara con el espacio
print("hola " + "python")

# Esto me muestra un error
# print("hola " + 4)

# Repetir texto con *
print("string" + str(5))
print("hola " * 5)
print("hola " * int(2.5))

# operadores conparativos con numeros

print(3 > 4)   # False
print(3 < 4)   # True
print(3 >= 4)  # False
print(3 <= 4)  # True
print(3 == 4)  # False
print(3 != 4)  # True

# operadores ocmparativos con strings
print("Como funcionan las comparaciones entre strings")

print("hola" > "python")    # False (compara por unicode)
print("hola" < "python")    # True
print("hola" >= "hola")     # True
print("aaaa" > "abaa")      # False (orden alfabetico)
print(len("aaaa") > len("abaa"))  # False (cuenta caracteres)
print("hola" <= "python")   # True
print("hola" == "hola")     # True
print("hola" != "python")   # True
print("Operadores Logicos")

# operadores logicos: and, or

print(3 > 4 and "hola" > "python")   # False and False = False
print(3 > 4 or "hola" > "python")    # False or False = False
print(3 < 4 and "hola" < "python")   # True and True = True
print(3 < 4 or "hola" > "python")    # True or False = True

# prioridad de operadores
print(3 > 4 or ("Hola" > "Python" and 4 == 4))

# operadores not
print("Operador Not")
print(not(3 > 4))

# ejemplo de mis datos
mi_edad = 25
edad_minima_conducir = 18
print(f'Tengo edad para conducir? {mi_edad >= edad_minima_conducir}')