# 1. Crea un nuevo archivo en tu entorno de trabajo llamado actividad_listas2.py.
# 2. Declara una lista llamada precios que contenga al menos seis valores numéricos (pueden representar precios de productos o servicios). o Asegúrate de incluir al menos un valor repetido.
precios = [10, 20, 30, 40, 50, 50, 20]
# 3. Crea otra lista llamada empleado con cuatro datos distintos: o nombre, edad, puesto de trabajo y ciudad.
empleados = ['Sebastian', 25, 'Programador', 'Leon']
# (Ejemplo: [&quot;Lucía&quot;, 29, &quot;Diseñadora&quot;, &quot;Barcelona&quot;])
# 4. Analiza las listas:
# o Muestra ambas listas con print().
print(precios)
print(empleados)
# o Usa len() para mostrar cuántos elementos tiene cada lista.
print(len(precios))
print(len(empleados))
# o Usa type() para verificar el tipo de dato.
print(type(precios))
print(type(empleados))
# 5. Accede a elementos específicos:
# o Muestra el primer, tercer y último elemento de la lista empleado.
print("Primer elemento:", empleados[0])
print("Segun elemento:", empleados[2])
print("Tercer elemento:", empleados[3])
# o Usa índices negativos para acceder al penúltimo elemento.
print("Penultimo elemento", empleados[-2])
# 6. Actualiza información:
# o Cambia la ciudad o el puesto de trabajo del empleado.
empleados[3] = 'Colombia'
print(empleados)
# o Agrega un nuevo elemento con .append() (por ejemplo, un departamento o área).
empleados.append('Antioquia')
print(empleados)
# o Inserta un nuevo dato en la segunda posición con .insert() (por ejemplo, un número de empleado).
empleados.insert(2, 1234)
print(empleados)
# 7. Elimina información:
# o Usa .remove() para quitar un precio específico de la lista precios.
precios.remove(10)
print(precios)
# o Usa .pop() para eliminar el último precio e imprimir el valor eliminado.
print(precios.pop())
print(precios)
# o Usa del para eliminar el segundo elemento de la lista empleado.
del empleados[1]
print(empleados)
# 8. Combina listas:
# o Crea una nueva lista llamada datos_empresa que combine empleado y precios usando el operador +.
datos_empresa = empleados + precios
# o Muestra el resultado.
print(datos_empresa)
# 9. Aplica métodos de listas:
# o Usa .count() para contar cuántas veces se repite un mismo precio.
print(precios.count(50))
# o Usa .copy() para duplicar la lista precios antes de vaciarla con .clear().
print(precios.copy())
print(precios.clear())
# o Imprime ambas listas para comparar.
print(precios)
print(empleados)
# 10. Ordena y reorganiza:
# o Crea una lista llamada ventas con números enteros y ordénala demenor a mayor con .sort().
ventas = [432,5665,3432,76,65,32,5,67,32,8,87,6,3,543,1]
ventas.sort()
print(ventas)
# o Luego invierte el orden con .reverse() y muestra el resultado final.
ventas.reverse()
print(ventas)
# Crea una lista llamada lenguajes con los lenguajes de programación que te gustaría aprender.
lenguajes = ['ingles', 'frances', 'aleman', 'italiano']
#  Muestra solo los dos primeros usando slicing ([:2]).
print(lenguajes[:2])
#  Cambia uno por otro que ya conozcas.
lenguajes[1] = 'Español'
print(lenguajes)
#  Agrega un nuevo lenguaje al final y elimina el primero.
lenguajes.append('Arabe')
print(lenguajes)
lenguajes.pop()
print(lenguajes)


