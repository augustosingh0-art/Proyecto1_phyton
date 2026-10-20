puntajes = []
numeros = int(input("Ingrese 5 puntajes: "))

for i in range(numeros):
    dato = str(input(f"Ingrese el puntuaje {i+1}: "))
    puntajes.append(dato)
    puntajes.sort()
    puntajes.reverse()



print(f"podio= 1er lugar {puntajes[0]} , 2do luegar {puntajes[1]} , 3er lugar {puntajes[2]}")