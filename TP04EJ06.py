from funciones import suma ,porcentaje

cvarones = int(input("Ingrese la cantidad de varones del curso: "))
cmujeres = int(input("Ingrese la cantidad de mujeres del curso: "))


total = suma(cvarones, cmujeres )

totalh = porcentaje(cvarones,total)

totalf = porcentaje(cmujeres,total)
print(f"Cantidad de varones {totalh}")
print(f"Cantidad de mujeres {totalf}")