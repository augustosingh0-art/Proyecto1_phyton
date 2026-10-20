materiales = []
cantidad = int(input("¿Cuántos materiales desea ingresar?: "))

for i in range(cantidad):
    material = input(f"Ingrese material nro{i+1}: ")
    if material in materiales: 
        print("El material ya fue agregado")
        continue
    materiales.append(material)

for i in range(len(materiales)):
    print(i + 1, "*", materiales[i])

print(f"cantidad de materiales: {len(materiales)}")

materiales.sort()

print(f"Materiales ordenados alfabeticamente: {materiales}")
