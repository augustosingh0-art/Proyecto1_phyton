inicio = str(input("Ingrese su contraseña: "))
contra = len(inicio)
if contra <8 :
    print("Es una contraseña corta.")
elif contra > 8 :
    print("Es una contraseña larga.")

if contra == 8 :
    print("Contraseña correcta.")