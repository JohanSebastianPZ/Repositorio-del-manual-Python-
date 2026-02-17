# Condicion simple 
horasTrabajadas = 100

if horasTrabajadas > 0:
    print('Las horas fueron registradas correctamente')

# Uso de if y else
horaLlegadaEmpleado = 10

if horaLlegadaEmpleado > 8:
    print('El empleado llego puntual al trabajo')
else:
    print('El empleado llego tarde al trabajo')

# Operadores logicos
horasTrabajadas = 20

if horasTrabajadas >= 0 and horasTrabajadas <= 12:
    print('Rango correcto de horas')
else:
    print('Rango incorrecto las horas deben estar en un rango de 0 a 12')

# Uso de elif
minutosRetraso = 1

if minutosRetraso == 2:
    print('Llegaste un poco tarde')
elif minutosRetraso == 5:
    print('Ojo, ya vas tarde')
else:
    print('Ya pa que vienes, mejor quedate en casa')

# Strings en condicionales
mensajeExcusa = 'mensaje'

if mensajeExcusa == '':
    print('Motivo no registrado porque la cadena esta vacia')
else: 
    print('Motivo registrado')

# Uso de not
horaSalida = 16

if not horaSalida:
    print('Salida no registrada')
else:
    print('Salida registrada')