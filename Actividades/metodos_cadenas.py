
# Escribe un programa en Python que almacene una palabra en la variable language y 
# muestre por pantalla la siguiente información utilizando métodos de cadenas:

texto = "texto de prueba"

# 1. La palabra con la primera letra en mayúscula.
print(texto.capitalize())
# 2. La palabra completamente en mayúsculas.
print(texto.upper())
# 3. Cuántas veces aparece la letra en la palabra.
print(texto.count("e"))
# 4. Si la palabra está formada únicamente por números.
print(texto.isnumeric())
# 5. Una comprobación numérica usando el texto "1".
print("1".isnumeric())
# 6. La palabra en minúsculas.
print(texto.lower())
# 7. Si la palabra está completamente en mayúsculas.
print(texto.upper().isupper())
# 8. Si la palabra comienza con "py".
print(texto.startswith("py"))
