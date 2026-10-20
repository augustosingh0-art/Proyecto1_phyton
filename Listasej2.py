numeros = []
num = int(input("¿Cuantos numeros desea ingresar: ? "))
for i in range(num):
    num = int(input("Ingrese el numero: "))
    numeros.append(num)
    numeros.sort()

print(numeros)
