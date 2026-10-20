a = int(input(f"Ingrese el primer lado de su triangulo: "))
b = int(input(f"Ingrese el segundo lado "))
c = int(input(f"Ingrese el tercer lafo: "))
if a == b and b == c :
    print("Su triangulo es equilatero.")
elif a== b or a== c or b == c:
    print("Su triangulo es Isoceles")
else:
    print("Su triangulo es escaleno.")