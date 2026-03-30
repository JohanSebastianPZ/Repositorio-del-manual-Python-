# Esta funcion se encarda de pedir la edad y verifica si es un dato valido.
def pedir_edad(mensaje):
    dato = input(mensaje)
    if not dato.isdigit() or int(dato) < 0 :
        raise ValueError('Debes ingresar un datos numerico valido');
    return int(dato)

# Esta funcion se encarga de cambia el correo del usuario buscado por indice
def cambio_correo(usuarios):
    user_id = int(input('Ingrese el id del usuario: '))
    # Verificamos si el user_id es valido y si esta dentro del rango de los usuarios
    if user_id >= 0 and user_id < len(usuarios):
        nuevo_email = input('Nuevo correo: ')
        # actualizamos el correo del usuario por su indice
        usuarios[user_id].email = nuevo_email
        print('\n-> EMAIL ACTUALIZADO CORRECTAMENTE')
    else:
        raise ValueError('No se encontro ID')