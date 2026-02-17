print("Hola" < "Python")
print("Hola" > "Python")
print("Hola" >= "Hola")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

#Preguntas de análisis
#1. ¿Qué resultado obtuviste en cada comparación?

True
False
True
True
True
True

#2. ¿Por qué Hola < "Python" devuelve True y "Hola" > "Python" devuelve False?

print("(Hola < Python = True) - Esto para porque python compara el orden alfabetico basado en los valores unicode de cada caracter (H = 72 < P = 80) (72 < 80 = True) y por eso da True el resultado")

#3. ¿Qué sucede si cambias "Hola" por "hola" (con minúscula)?

print("hola" < "Python")
print("(hola < Python = False) - Esto para porque python compara el orden alfabetico basado en los valores unicode de cada caracter (h = 104 < P = 80) (104 < 80 = False) y por eso da False el resultado")

#4. ¿Por qué "Hola" == "hola" da False aunque parecen iguales?

print("Hola" == "Hola")
print("( Hola == Hola = True) - Esto para porque python compara el orden alfabetico basado en los valores unicode de cada caracter (H = 72 == H = 72) (72 == 72 = True) y por eso da True el resultado")

#5. ¿Qué crees que hace Python internamente para comparar dos textos?

print("Esta pasa porque al momento de hacer la comparacion de textos se compara su valor unicode, lo los significados de las palabras")

#6. Escribe en el intérprete lo siguiente y anota el resultado:

print(ord("H"))
print(ord("P"))

#¿Qué representan esos números?

print("Estos son los valores unicode de la letra: H = 72")
print("Estos son los valores unicode de la letra: P = 80")

#9. Cambia las palabras y prueba con ejemplos como:

print("a" < "b")
print("Z" < "a")
print("Casa" > "casa")
print("Python" > "Py")

#Explica en tus palabras por qué se obtienen esos resultados.

True
True
False
True

print("(a < b = True) - Esto pasa porque Python compara el orden alfabetico basado en los valores Unicode de cada caracter: " + "ord('a') = " + str(ord('a')) + " < ord('b') = " + str(ord('b')) + ", y como 97 < 98, por eso da True.")
print("('Z' < 'a' = True) - Esto pasa porque Python compara el orden alfabético basado en los valores Unicode de cada caracter: " + "ord('Z') = " + str(ord('Z')) + " < ord('a') = " + str(ord('a')) + ", y como 90 < 97, por eso da True.")
print("('Casa' > 'casa' = False) - Esto pasa porque Python compara letra por letra: " + "ord('C') = " + str(ord('C')) + " y ord('c') = " + str(ord('c')) + ", y como 67 > 99, el resultado es False.")
print("('Python' > 'Py' = True) - Esto pasa porque Python compara carácter por carácter: las dos primeras letras ('P' y 'y') son iguales, pero 'Py' termina antes, así que la palabra más larga ('Python') se considera mayor. Resultado: True.")

