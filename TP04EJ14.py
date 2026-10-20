from funciones import triangulo

a = float(input("Ingrese el lado A: "))
b = float(input("Ingrese el lado B: "))
c = float(input("Ingrese el lado C: "))

resultado = triangulo(a, b, c)

print(f"El triangulo es: {resultado}")