nombre = "Nahuel"
print(f"tu nombre es {nombre}")
nom = str(input("Ingrese un nombre: "))
print(f"El nombre ingresado es {nom}")

num1 = 6
num2 = 3
total = num1 + num2
print(f"El resultado es {total}")
n1 = int(input("ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
resta = n1 - n2
print(f"la resta es {resta}")

nota = 8
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")
    
nt = int(input("inrese una nota: "))
if  nt >= 7 :
    print("promocionado ")
else:
    print("regular ")
    
n = 5 
if n>0:
    print("positivo")
elif n<0 :
    print("negativo")