from funciones import sueldo

nombre = input("Ingrese el nombre del empleado: ")
categoria = input("Ingrese la categoría (A o B): ").upper()

sueldo = sueldo(categoria)

if sueldo is not None:
    print(f"Empleado: {nombre}")
    print(f"Sueldo: $ {sueldo}" )
else:
    print("Categoria invalida")