"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 011_Clases.py
============================================================================
"""
# las clases son como el plano de una casa o un molde para galletas

# asi se hace una clase vacia que no hace nada todavia
class mi_persona_vacia:
    pass  # pongo pass para que python no se queje de que esta vacia


# si imprimo esto solo me dice que existe el molde
print(mi_persona_vacia)


# al poner los parentesis es cuando fabrico el objeto real
print(mi_persona_vacia())


# el constructor init es la clave de todo
# se activa solo en cuanto creas el objeto para darle sus datos iniciales

class persona:
    def __init__(self, nombre, apellido):
        pass


# aqui usamos self que es como decir este objeto en concreto
# sirve para guardar los datos dentro de cada copia que hagamos

class persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# ahora creamos a sebastian usando el molde de persona
mi_persona = persona("sebastian", "martinez")
print(f"{mi_persona.nombre} {mi_persona.apellido}")


# tambien podemos mezclar datos y crear funciones propias de la clase
# a estas funciones dentro de clases las llamamos metodos

class persona:
    def __init__(self, nombre, apellido):
        # guardamos el nombre completo de una vez
        self.nombre_completo = f"{nombre} {apellido}"
    
    def caminar(self):
        # usamos self para que sepa de que persona estamos hablando
        print(f"{self.nombre_completo} esta caminando")


# vamos a probar el objeto con su metodo

# fabricamos a sebastian
mi_persona = persona("sebastian", "martinez")

# miramos su variable interna
print(mi_persona.nombre_completo)

# hacemos que ejecute su accion de caminar
mi_persona.caminar()


# los datos de los objetos se pueden cambiar despues de crearlos

# empezamos con sebastian otra vez
mi_persona = persona("sebastian", "martinez")

print(mi_persona.nombre_completo)
mi_persona.caminar()

# le cambiamos el nombre a la fuerza desde fuera
mi_persona.nombre_completo = "carlos el loco de los gatos"

# ahora el objeto ya no se llama sebastian se ha actualizado
print(mi_persona.nombre_completo)

# si camina ahora saldra con el nombre nuevo
mi_persona.caminar()

