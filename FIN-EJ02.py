codigoc = "EST2026"
intentos = 0
while intentos < 3:
    codigo = input("Ingrese el codigo de socio: ")
    if codigo == "":
        print("El codigo no puede estar vacio")
        continue

    intentos += 1

    if codigo == codigoc:
        print("Acceso permitido")
        break
    else:
        print(f"Código incorrecto, intento {intentos} de 3")

if intentos == 3 and codigo != codigoc:
    print("Acceso denegado, Consulte en preseptoria.")

