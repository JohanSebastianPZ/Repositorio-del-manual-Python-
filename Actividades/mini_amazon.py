CATALOGO = {
    "A001": {"nombre": "Teclado Mecánico", "precio": 49.99, "stock": 10, "peso_kg": 0.9},
    "A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
    "A003": {"nombre": 'Monitor 24"', "precio": 149.00, "stock": 3, "peso_kg": 3.5},
    "A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
    "A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
    "ENVIOFREE": {"tipo": "envio", "descuento": 1.0},
    "DESC10": {"tipo": "total", "descuento": 0.10},
}

CAR = {}
HISTORIAL_PEDIDOS = [] 

def main():
    print('\n1. Ver catálogo')
    print('2. Añadir producto al carrito')
    print('3. Quitar producto del carrito')
    print('4. Ver carrito')
    print('5. Confirmar pedido')
    print('0. Salir')
    
def mostrar_catalogo(catalogo):
    for producto in catalogo:
        datos = catalogo[producto]
        print(f'id: {producto}, Nombre: {datos['nombre']}, Precio: {datos['precio']}, Stock: {datos['stock']}, Peso: {datos['peso_kg']}')

# Aqui usamos el for else para verificar si el codigo ingresado por el usuario existe en el catalogo
def validar_codigo_producto(catalogo, codigo):
    for producto in catalogo:
        if producto == codigo:
            return True
    else:
        return False
            
def agregar_al_carrito(carrito, catalogo, codigo, cantidad):
    if validar_codigo_producto(catalogo, codigo):
        if int(cantidad) > catalogo[codigo]['stock']:
            print('No es posible agregar al carro de compra por falta de stock')
            return False

        if codigo in carrito:
            carrito[codigo] += cantidad
        else: 
            carrito[codigo] = cantidad
        return True
    else:
        print('El codigo no se encuentra en el catalogo')
        return False;
            
def calcular_totales(carrito, catalogo, iva=0.21):

    peso = 0
    subtotal = 0
    
    for codigo, cantidad in carrito.items():
        datos_prod = catalogo[codigo]
        subtotal += cantidad * datos_prod['precio']
        peso += cantidad * datos_prod['peso_kg']

    # Calculo para el iva_total
    iva_aplicado = (subtotal * iva)
    total = subtotal + iva_aplicado

    totales = {'subtotal':subtotal, 'iva':iva_aplicado, 'peso':peso, 'total': total}
        
    return totales
        
def calcular_envio(peso_total, zona="PENINSULA"):

    coste_envio = 0
    
    if peso_total >= 2.0:
        coste_envio = 10
    elif peso_total >= 1.5 and zona=='BALNEARES':
        coste_envio = 10
    elif peso_total >= 1.0:
        coste_envio = 8
    elif peso_total >= 0.5:
        coste_envio = 6
    else:
        coste_envio = 4
        
    return coste_envio

def aplicar_promos(total, envio, *codigos):
    for codigo in codigos:
        codigo = codigo.upper()
        
        # Validacion existencia del codigo en las promos
        if codigo in CODIGOS_PROMO:
            datos_promo = CODIGOS_PROMO[codigo]
            
            # 2. Diferenciamos qué descuento aplicar
            if datos_promo['tipo'] == 'total':
                total -= (total * datos_promo['descuento'])
            elif datos_promo['tipo'] == 'envio':
                envio = 0  
        else:
            print(f"Código promocional {codigo} no válido.")

    # 3. Devolvemos AMBOS valores actualizados
    return total, envio
            
opcion = ''
cont_product = 6

while(opcion != '0'):
    main()
    opcion = input('Seleccione opcion: ')

    if opcion == '1':
        print('\n=== Ver Catalogo ===\n')
        mostrar_catalogo(CATALOGO)
    elif opcion == '2':
        print('\n=== Añadir producto ===')
        codigo = input('Ingrese el codigo del producto para ingresarlo al carrito: ')
        cantidad = int(input('Ingrese la cantidad de productos a agregar al carrito: '))
        if(agregar_al_carrito(CAR, CATALOGO, codigo, cantidad)):
            print('\n=== PRODUCTO AGREGADO AL CARRITO CON EXITO ===')
        else:
            print('\n=== OCURRIO UN PROBLEMA, NO SE PUDO AGREGAR AL CARRITO EL PRODUCTO ===')
    elif opcion == '3':
        print('\n=== Quitar producto===')
        codigo_eliminar = input('Ingrese el codigo del producto que desea eliminar: ')
        if codigo_eliminar in CAR:
            # Aqui necesito agregar de que elimine por unidad, no todo
            del CAR[codigo_eliminar]
            print('Producto eliminado con exito')
        else:
            print('Este codigo no esta relacionado a ningun producto')
        print('\n=== PRODUCTO QUITADO DEL CARRITO CON EXITO ===')
    elif opcion == '4':
        print('\n=== Ver carrito ===\n')    
        # Verificacion existencia productos en el carrito
        if CAR:
            for codigo, cantidad in CAR.items():
                datos_prod = CATALOGO[codigo]
                print(f'Id: {codigo}, Nombre: {datos_prod['nombre']}, Precio: {datos_prod['precio']}, Peso: {datos_prod['peso_kg']}, Cantidad: {cantidad}')
        else:
            print('El carro no tiene productos en este momento')
    elif opcion == '5':
        print('\n=== Confirmar pedido ===\n')
        
        if CAR:
            # Resumen de lo que existe en el carro
            for codigo, cantidad in CAR.items():
                datos_prod = CATALOGO[codigo]
                print(f'Id: {codigo}, Nombre: {datos_prod["nombre"]}, Cantidad: {cantidad}')

            resumen = calcular_totales(CAR, CATALOGO)
            costo_envio = calcular_envio(resumen['peso'])
            
            # Variables finales
            total_final = resumen['total']
            envio_final = costo_envio
            
            # Verificar promociones
            cupon_insert = input('\nIngrese cupón (o "n" para omitir): ').upper()
            if cupon_insert != 'n':
                total_final, envio_final = aplicar_promos(total_final, envio_final, cupon_insert)
            
            # Aqui calculamos el precio total definitivo
            precio_total_real = total_final + envio_final
            
            print(f'\nSubtotal (sin IVA): {resumen["subtotal"]:.2f}€')
            print(f'IVA aplicado (21%): {resumen["iva"]:.2f}€')
            print(f'Peso total: {resumen["peso"]} kg')
            print(f'Coste envío: {envio_final:.2f}€')
            print(f'== PRECIO TOTAL A PAGAR: {precio_total_real:.2f}€ ==')

            # Confirmacion transaccion
            opcion_compra = input('\n¿Desea confirmar la transacción (y/n)?: ').lower()
            
            if opcion_compra == 'y':
                # Descontar stock del catálogo
                for cod, cant in CAR.items():
                    CATALOGO[cod]['stock'] -= cant
                
                # Guardar registro en historial
                registro = {
                    'estado': 'CONFIRMADO', 
                    'productos': CAR.copy(), # Copiamos el contenido actual
                    'total': precio_total_real
                }
                HISTORIAL_PEDIDOS.append(registro)
                CAR.clear() # Vaciamos el carrito tras la compra exitosa
                print('Compra realizada con éxito, pedido CONFIRMADO.')
                
            else:
                # Si el usuario pone 'n' o cualquier otra cosa, se cancela
                registro = {
                    'estado': 'CANCELADO', 
                    'productos': CAR.copy(), 
                    'total': 0
                }
                HISTORIAL_PEDIDOS.append(registro)
                print('COMPRA CANCELADA.')
            
        else:
            print('El carro no tiene productos en este momento.')
                
    elif opcion == '0':
        print('\n=== Fin del programa ===\n')
        print("\n=== INFORME FINAL DE VENTAS ===\n")
        
        # Aqui muestro todos los productos
        if not HISTORIAL_PEDIDOS:
            print("No se registraron movimientos en el sistema.")
        else:
            for pedido in HISTORIAL_PEDIDOS:
                print(f"Pedido {pedido['estado']} - Importe: {pedido['total']}\n")
    else:
        print('ERROR: Opcion incorrecta')
