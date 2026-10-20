a = int(input("Ingrese el primer número para ordenarlos de mayor a menor: "))
b = int(input("Ingrese el segundo número "))
c = int(input("Ingrese el tercer número "))
if a >= b and b >= c :
    mayor = b
    if a >= c :
        medio = a
        menor = c
    else:
        medio = c
        menor = a
elif b >= a and b >= c :
    mayor = c
    if a >= c:
        medio = a
        menor = b 
    else:
        medio = c
        menor = a
else:
    mayor = c
    if a >= b:
        medio = a
        menor = b 
    else:
        medio = b
        menor = a 

print("El mayor es: " , mayor)
print("El medio es: " , medio)
print("El menor es: " , menor)