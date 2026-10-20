from funciones import operar

a = float(input("Ingrese A: "))
b = float(input("Ingrese B: "))

if b == 0 and a < b:
    print("No se puede dividir por cero")
else:
    resultado = operar(a, b)
    print(f"Resultado: {resultado}")