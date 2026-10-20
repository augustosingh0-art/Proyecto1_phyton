nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
if edad <= 5 :
    etapa = "Infancia"
elif edad <= 11:
    etapa = "Niñez"
elif edad <= 17:
    etapa = "Adolescencia" 
elif edad <= 59:
    etapa = "Adultez "
else:
    etapa = "Vejez"

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Etapa de la vida: {etapa}")