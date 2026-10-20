pal1 = str(input("Ingrese la primera palabra: "))
pal2 = str(input("Ingrese la segunda palabra: "))
if len(pal1) > len(pal2) :
    print("La primera palabra ingresada es más larga que la segunda.")
elif len(pal2) > len(pal1) :
    print("La segunda palabra ingresada es más larga que la primera")
else:
    print("ambas palabras tienen misma lngitud de caracteres.")
