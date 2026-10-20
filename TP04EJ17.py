from funciones import ordenartres

a = float(input("Ingrese el primer numero para ordenarlos de mayor a menor: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

mayor, medio, menor = ordenartres(a, b, c)

print("Los numeros ordenados son: ")
print(mayor)
print(medio)
print(menor)