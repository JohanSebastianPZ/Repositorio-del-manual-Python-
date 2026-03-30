# Creamos una clase con atributos privados
class Usuario: 
        def __init__(self, nombre, edad, email):
            self.nombre = nombre
            self.edad = edad
            self.email = email

        # ============== Nombre ==============
        @property 
        def nombre(self):
            return self.__nombre
        
        @nombre.setter
        def nombre(self, valor):
            if " " in valor:
                raise ValueError('Nombre no puede contener espacios en blanco')
            valor_limpio = valor.strip()
            if not valor_limpio:
                raise ValueError('Nombre no puede estar vacio')
            self.__nombre = valor
        
        # ============== Edad ==============
        @property
        def edad(self):
            return self.__edad
        
        @edad.setter
        def edad(self, valor):
            if valor % 2 != 1 and valor <= 0:
                raise ValueError('La edad debe ser un numero entero mayor que 0')
            self.__edad = valor
            
        # ============== Email ==============
        @property
        def email(self):
            return self.__edad
        
        @email.setter
        def email(self, valor):
            if '@' not in valor or "." not in valor:
                raise ValueError('Email invalido debe contener @ y .')
            self.__email = valor
            
        # ============== str ==============
        def __str__(self):
            return f"Usuario: {self.__nombre} | Edad: {self.__edad} | Email: {self.__email}"

# print(admin.__email) # Asi no puedo acceder porque python renombre la variabla internamente.
# print(admin._Usuario__email) # Esta es la forma en la que podria acceder