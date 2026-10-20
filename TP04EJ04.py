from funciones import promedio

a = int(input("Ingrese el primer nro: "))
b = int(input("Ingrese el segundo nro: "))
c = int(input("Ingrese el tercer nro: "))
d = int(input("Ingrese el cuarto nro: "))
e = int(input("Ingrese el ultimo nro: "))

q = promedio(a,b,c,e,d)

print(f"Su promedio es {q}")