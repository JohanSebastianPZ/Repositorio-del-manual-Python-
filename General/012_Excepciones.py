"""
============================================================================
    Estudiante: Johan Sebastian Neiva Martinez
    Asignatura: MODULO OPTATIVO
    Profesora: Geraldin López
    Archivo: 012_Excepciones.py
============================================================================
"""

numberOne = 12
numberTwo = 10 
try:
    print(numberOne + int(numberTwo))
    print('No se ha produco un error')
except:
    print('Se ha prducido un error')

try:
    print(numberOne + numberTwo)
    print('No se ha producido un error')
except:
    # Esto se ejecuta si ocurrio un error
    print('Se ha producido un error')
else:
    # Esto se ejecuta correctamente
    print('La ejecucion continua correctamente')
finally:
    # Esto se ejecuta siempre
    print('Fin del bloque de control de excepciones')
    
# Esto es para especificar cada tipo de error, para tener un control, de cada tipo de error que se presenta
try:
    print(numberOne + numberTwo)
except ValueError:
    print('Se ha producido un error ValueError')
except TypeError:
    print('Se ha productido un error TypeError')

try:
    print(numberOne + numberTwo)
    print('NO se produjo ningun error')
    # Asi es como puedo especificar el tipo de error que se me presenta
except ValueError as a:
    print(f'Ocurrio un error{a}')

