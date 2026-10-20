from funciones import producto,cociente

a = int(input("Ingrese un nro: "))
b = int(input("Ingrese otro nro: "))
c = producto(a,b)
d= cociente(a,b)

print(f"cociente = {d}")
print(f"Producto = {c}")