from funciones import sexo

nom = str(input("Ingrese su nombre: "))
s = str(input("Ingrese su sexo (M ó F): " ))

a = sexo(s)

print(f"El sexo es {s}")