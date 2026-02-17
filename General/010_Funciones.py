"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 010_funciones.py
============================================================================
"""

# las funciones sirven para guardar codigo y usarlo cuando quieras
def mi_funcion():
    print("esto es una funcion")

# aqui la llamamos para que se ejecute
mi_funcion()

# funcion con parametros para sumar dos cosas
def sumar_dos_valores(primer_numero, segundo_numero):
    print(primer_numero + segundo_numero)

sumar_dos_valores(1, 1)

# poner el tipo de dato es solo una ayuda visual para el editor
# python no te obliga a cumplirlo a rajatabla
def sumar_dos_valores_con_tipo(primer_numero: int, segundo_numero: int):
    print(primer_numero + segundo_numero)

# por eso esto concatena los strings en vez de dar error
sumar_dos_valores_con_tipo("4", "5")

# usar return sirve para que la funcion te devuelva el dato
# asi puedes guardarlo en una variable y usarlo luego
def sumar_con_retorno(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

print(sumar_con_retorno(10, 5))
mi_resultado = sumar_con_retorno(10, 4)
print(mi_resultado)

# funcion para imprimir nombres usando f-strings
def imprimir_nombre(nombre, apellido):
    print(f"{nombre} {apellido}")

imprimir_nombre("sebastian", "martinez")

# puedes cambiar el orden si dices que valor va a cada clave
imprimir_nombre(surname="sebastian", name="martinez")

# parametro por defecto por si te falta algun dato al llamar la funcion
def imprimir_con_alias(nombre, apellido, alias="sin alias"):
    print(f"{nombre} {apellido} {alias}")

# aqui como no paso el alias usa el que pusimos por defecto
imprimir_con_alias("sebas", "lopez")

# el asterisco sirve para pasar todos los textos que quieras
# se convierte en una especie de lista que puedes recorrer
def imprimir_textos_en_mayus(texts):
    for texto in texts:
        print(texto.upper())

imprimir_textos_en_mayus("hola", "python", "prefegeraly")
imprimir_textos_en_mayus("hola")

print("\n=== fin de la parte de funciones ===")