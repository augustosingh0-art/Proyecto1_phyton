n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese otro numero: "))
if n1 < n2:
    inicio = n1
    final = n2
else:
    inicio = n2
    final = n1

for i in range(inicio,final):
    print(i)