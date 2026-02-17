# Johan Sebastian Neiva Martinez
# Sergio Valenzuela Martel

#final
usunom = input("Ingresa el nombre: ")
usuedad = int(input("Ingresa edad: "))
usuciudad = input("Ingresa ciudad: ")

datosUsuario = [usunom, usuedad, usuciudad]
print(datosUsuario)

print(f"Me llamo {usunom} tengo {usuedad} años y vivo en {usuciudad}")
print(len(datosUsuario))

hobbie1 = input("Introduce un hobbie: ")
hobbie2 = input("Introduce otro hobbie: ")
hobbies = [hobbie1, hobbie2]

informacionCompleta = datosUsuario + hobbies
print(informacionCompleta)

print(f"Me llamo {usunom}, tengo {usuedad} años y una de mis aficiones es {hobbie1}")
