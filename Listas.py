#listas se crean con corchetes 
#indice     0 1 2 3 4
#´se pueden hacer listas vacias

alumnos = ["Ana" , "Juan", "Miguel", "Diego"]
#print(nombres[-1])

#para generar corchetes necesito alt + 91 y cerrar alt + 93
#print([-1]) = visualizar el ultimo dato
#para el anteultimo es -2, -3 ,etc...

elementos = len(alumnos)-1
print(elementos)

#añadir elementos a una lista
#se usa append

alumnos.append("Elena")
print(alumnos)

#insert = añade elementos en una ub especifica

alumnos.insert(2, "Jose")
print(alumnos)

#añadir más = #extend

nuevos = ["Augusto" , "Nahuel"]
alumnos.extend(nuevos)
print(alumnos)

#modificar algun elemento

alumnos[0] = "Antonella"
print(alumnos)

#eliminar = remove

alumnos.remove("Miguel")
print(alumnos)

#eliminar por un indice en especifico = pop

alumnos.pop(0)
print(alumnos)

#se elimina el ultimo registro si en el .pop() no hay nada
#tambien se puede usar alumnos.pop(-1)

alumnos.pop()
alumnos.pop(-1)
print(alumnos)

#para vaciar la lista se usa .clear

#alumnos.clear()
#print(alumnos) 

#-----

numeros = [2,5,10,7,12]

cant = len(numeros)
print(cant)

if 1 in numeros:
    print("Tienes 1 ")
else:
    print("No tienes 1 ")


#el in verifica si el valor esta en la lista
#mediante el tambien se verifican datos 

ubi = alumnos.index("Juan")
print(ubi)

#ubicamos en que indice etsa Juan , el index ubica

notas = [10,9,10,7,1,10]

#count cuenta los valores del indice 
diez = notas.count(10)
print(diez)

#para ordenar de menor a mayor se usa sort

numeros.sort()
print(numeros)

#para darla vuelta se usa reverse

numeros.reverse()
print(numeros)

#sorted devuelve una lista nueva sin modificar la original

cal = sorted(notas)
print(cal)


#con ciclos:

for i in numeros:
    print(i)

for nota in notas:
    print(nota)


#con len():

for i in range (len(notas)):
    print(f"Calificacion {i+1}: {notas[i]}")

#la iteracion +1 para ordenar

for i in range(len(alumnos)):
    print(f"Alumno {i+1}: {alumnos[i]}")

equipo = []

