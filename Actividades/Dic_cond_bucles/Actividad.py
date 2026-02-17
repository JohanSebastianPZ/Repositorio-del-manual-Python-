# Cada alunmo tendra:
# Nombre
# Edad
# Curso
# Lenguajes(set)
# Nota media

# Parte 1
alumnos = {}

alumnos['Sebastian'] = {
        'edad': 25, 
        'curso': 'DAW2',
        'lenguajes': {'java', 'php', 'javascript', 'python'}, 
        'nota': 5.5
}

alumnos['Tatiana'] = {
        'edad': 30, 
        'curso': 'DAM2',
        'lenguajes': {'java', 'php', 'javascript', 'python', 'react', 'Angular'}, 
        'nota': 8.5
}   

alumnos['Diego'] = {
        'edad': 35, 
        'curso': 'DAW2',
        'lenguajes': {'java', 'C', 'C++', 'Microservidores'}, 
        'nota': 10.0
}

opcion = "" 
# Parte 5
while opcion != "4":
    print("\n--- MENÚ DE GESTIÓN ---")
    print("1. Mostrar alumnos")
    print("2. Buscar alumno")
    print("3. Añadir alumno")
    print("4. Salir")
    
    opcion = input("Seleccione su opción: ")

    if opcion == "1":
        # Parte 2
        print("\n=== LISTADO DE ALUMNOS ==")
        for nombre in alumnos:
            datos = alumnos[nombre]
            print()
            print(f"Nombre: {nombre}")
            print(f"Edad: {datos['edad']}")
            print(f"Curso: {datos['curso']}")
            for lenguaje in datos['lenguajes']:
                print(f"Lenguaje: {lenguaje}")
            # Parte 3
            print(f"Nota media: {datos['nota']} -> ", end="" )
            if datos['nota'] < 5:
                print('Suspenso')
            elif datos['nota'] >= 5 and datos['nota']< 7:
                print('Aprobado')
            elif datos['nota'] >= 7 and datos['nota']< 9:
                print('Notable')
            elif datos['nota'] >= 9:
                print('Sobresaliente')

        # Muestra todos los alumnos que sean mayores de 18 y que tengan una nota superior a 7
        # Parte 4
        print('\n === Alumnos Destacados (Mayores de 18 y con nota > a 7)')
        for nombre in alumnos:
            datos = alumnos[nombre]    
            if datos['edad'] > 18 and datos['nota'] > 7:
                print(f'Alumnos mayores de 18 y con nota superios a 7:', nombre)
                print() 

    elif opcion == "2":
        # Parte 6
        buscar = input("Introduce el nombre del alumno a buscar: ")
        info = alumnos.get(buscar)
        
        if info:
            print(f"Alumno: {buscar}\nEdad: {info['edad']}\nCurso: {info['curso']}\nNota: {info['nota']}")
        else:
            print("Alumno no encontrado")

    elif opcion == "3":
        print("\n=== REGISTRAR NUEVO ALUMNO ===")
        nombre = input("Nombre (o escribe salir para cancelar): ")

        if nombre.strip().lower() == "salir":
            print("Acción cancelada. Volviendo al menú...")
            opcion = "" 
            continue

        edad = int(input("Edad: "))
        curso = input("Curso: ")
        
        # Parte 7
        lenguajes_input = input("Lenguajes (separados por comas): ")
        lenguajes_set = set(lenguajes_input.split(","))
        
        nota = float(input("Nota media: "))

        alumnos[nombre] = {
            'edad': edad,
            'curso': curso,
            'lenguajes': lenguajes_set,
            'nota': nota
        }
        print(f"Alumno {nombre} añadido con éxito.")

    elif opcion == "4":

        total_notas = 0

        for nombre in alumnos:
            total_notas += alumnos[nombre]['nota']

        # Aqui divido el total de las notas con el total de los alumnnos
        media = total_notas / len(alumnos)
        print("=== MEDIA DE LA CLASE: ", media, " ===")
        print("Fin del programa")
    
    else:
        print("Opción no válida, intenta de nuevo.")