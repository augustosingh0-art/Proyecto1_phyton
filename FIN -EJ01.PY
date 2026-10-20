nombre = str(input("Ingrese el nombre completo del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))
promedio = int((input("ingrese el promedio de si escuela anterior: ")))

print(f"Bienvenido {nombre} !")
if promedio >= 7 :
    print("Felicidades,su ingreso es directo.")
elif promedio >= 4 :
    print("Debe rendir equivalencias.")
else:
    print("Debe cursar un curso de apoyo.")

    