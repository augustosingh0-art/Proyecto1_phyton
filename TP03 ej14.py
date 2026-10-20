secreto = 5
while True:
    num = int(input("Ingrese un número del 1 al 10:"))
    if num == secreto:
        print("Es el número correcto")
        break
    else:
        print("No es el número correcto, intente nuevamente")