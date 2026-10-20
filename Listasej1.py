nombres = []
cantidad = int(input("¿Cuantos nombres quiere ingresar?:"))

for i in range(cantidad):
    nom = str(input(f"Ingrese nombre {i+1}:"))
    nombres.append(nom)

print(nombres)