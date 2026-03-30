# importo la clase de usuarios que esta en el archivo usuario.py
import usuario
import utils

# Creo lista usuarios
usuarios = list()

# Creo usuarios
admin = usuario.Usuario('sebastian', 25, 'sebastian@gmail.com')
user_default = usuario.Usuario('default', 1, 'default@gmail.com')

# Agrego usuarios
usuarios.append(admin)
usuarios.append(user_default)

bucle = True

while bucle:
    try:
        print('\n=====================================================================================\n')
        print('1. Crear usuario')
        print('2. Mostrar usuarios')
        print('3. Modificar datos de un usuario')
        print('4. Salir')
        opcion = int(input('Seleccione la accion a realizar: '))
        print('\n=====================================================================================\n')
        # Crear un usuario, aqui tengo que pedir los datos necesarios para la creacion del usuario
        if opcion == 1:
            print('======= DATOS NUEVO USUARIO =======\n')
            nombre = input('Nombre: ')
            edad = utils.pedir_edad('Edad: ') # Aqui uso la funcion que tengo como utilidad
            email = input('Email: ')
            nuevo_usuario = usuario.Usuario(nombre, edad, email)
            usuarios.append(nuevo_usuario)
            print('\n-> USUARIO AGREGADO CON EXITO')
        # Mostrar todos los usuario
        elif opcion == 2:
            print('======= USUARIOS =======\n')
            if not usuarios:
                print('\n-> NO HAY USUARIOS REGISTRADOS')
            else:
                # i = es el indice y u sera el objeto 
                for i, u in enumerate(usuarios):
                    print(f"[{i}] {u}")
        # Modificar datos de un usuario buscando el usuario por id
        elif opcion == 3:
            print('======= MODIFICAR EMAIL USUARIO =======\n')
            
            utils.cambio_correo(usuarios)
            
        # Salir del programa
        elif opcion == 4:
            break
        else:
            raise ValueError('OPCION INCORRECTA, SELECCIONE UNA OPCION VALIDA')
    except ValueError as a:
        print(f'\n======= ERROR: {a} =======')
    except Exception as e:
        print(f'\n======= ERROR INESPEDADO: {e} =======')
    else:
        print('\n======= EJECUCION EXITOSA =======')
    finally: 
        print('\n======= FINALY =======')