notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"Notas:", notas)
print(f"Promedio:", promedio)
if promedio >= 6:
    print("El estudiante esta aprobado")
else:
    print("El estudiante esta desaprobado")