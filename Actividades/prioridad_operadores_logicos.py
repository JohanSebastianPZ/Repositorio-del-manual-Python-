
print(10 < 20 and (5 != 5 or 3 < 4)) # True
print((7 >= 7 or 2 > 3) and (4 == 4)) # True
print((8 < 6 and "a" == "a") and (10 != 5)) # False
print((3 * 2 == 9 and 7 < 2) or ("Hola" < "Mundo")) # True
print((5 > 2 and 8 < 3) and ("Perro" != "Gato")) # False

print("===========================Not===========================")

print(not("a" == "a")) # False
print("Hola"  != "Python") # True
print(not("Hola"  != "Python")) # False 
print((5 > 2 and 8 < 3) and ("Perro" != "Gato")) # False
print((5 > 2 and 8 < 3) and not ("Perro" != "Gato")) # True


if not (4 < 2):
	print("Este es un mensaje para hacer la comprobacion")
else:
	print("Esto es otro mensaje de prueba")


