nombre = input(f"Nombre del alumno: ")
materia = input("Materia: ")
nota = int(input(f"Nota: "))
if nota >= 6:
    print(nombre , "aprobo" , materia)
else:
    print(nombre , "desaprobo" , materia)