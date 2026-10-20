a = float(input(f"Ingrese su primer nota para calcular su promedio "))
b = float(input(f"Ingrese la segunda nota: "))
c = float(input(f"Ingrece la tercera nota: "))
promedio = (a+b+c) / 3
if promedio >= 7 :
    print("Usted esta aprobado.")
elif promedio >= 4 :
    print("Usted va a diciembre.")
else: 
    print("Usted va a marzo.")