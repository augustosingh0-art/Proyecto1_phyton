mail = str(input("Ingrese su e-mail: "))
if "@" in mail and "." in mail:
    print("email valido")
else:
    print("email invalido")