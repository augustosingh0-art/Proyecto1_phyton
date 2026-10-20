palabras = []
cant = int(input("Ingrese cinco palabras: "))

for i in range(cant):
    dato = str(input(f"Ingrese la palabra {i+1}"))

if len(dato) > 5 :
    palabras.append(dato)


print(palabras)