n = int(input(F"Ingrese un numero: "))
if n < -5 or n > 100:
    n = n - 5
elif n >= 0 and n < 20:
    n = n + 50
elif n > 50:
    n = n * 2

print("El resultado es ", n)