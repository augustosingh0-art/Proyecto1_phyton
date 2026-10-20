#palabra = " hola mundo "
#nombre = "AUGUSTO"

#print(palabra.upper())
#upper = convierte todo a mayusculas 

#print(palabra.lower())
#lower = convierte todas a minusculas 

#print(palabra.strip())
#elimina espacios en blanco al principio y al final 

#print(palabra.capitalize())
#poner en mayuscula el primer carcter unicamente de la cadena 

#print(palabra.title())
#poner en mayuscula la primera letra/caracter de cada palabra 

#left = izquierda 
#para borrar el epacio de la izquierda:
#print(palabra.lstrip())
3#lo mismo con la derecha (right):
#print(palabra.rstrip())


#print(palabra.find("la"))
#buscar caracteres,retorna el valor del indice que se encuentra
#de lo ocntrario sale -1 

#print(palabra.replace("do", "dial"))
#el replace marca la cadena que se desea reemplazar y se inserta l nueva cadena de carcateres

#print("mun" in palabra)
#mediante true or false = boleanos , verifica los valores dentro del dato (palabra)

#print("mun" not in palabra) 
#opuesto a lo anterior

#--- practica: 

nombre = str(input("Ingrese su nombre: "))
nombre = nombre.strip()
if len(nombre) < 5 :
    print("Es un nombre demasiado corto")
elif "admin" in nombre.lower() :
    print("Ese nombre no esta permitido")
else:
    print(nombre.title(), "Ese nombre es valido")