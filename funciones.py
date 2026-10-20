def saludar(nombre):
    print(f"Bienvenido {nombre}")

def suma(a,b):
    return a+b 

def producto(a,b):
    return a*b

def cociente(a,b):
    return a/b

def promedio(a,b,c,d,e):
    return (a+b+c+d+e) / 5

def superficie(a,b) :
    return (a + b) /2

def porcentaje(valor,total):
    porc = valor*100/total
    return porc

def mayormenpr(a,b):
    if a > b :
        print(f"El mayor es {a} y el menor es {b}")
    else:
        print(f"El mayor es {b} y el mennor es {a}")

def sexo(a):
    if a.lower() == "m" :
        print("Masculino")
    else:
        print("Femenino")

def aprobado(a):
    if a >= 6 :
        print("Aprobado")
    else:
        print("Desaprobado")

def sueldo(categoria):
    if categoria == "A":
        return 500000
    elif categoria == "B":
        return 750000
    else:
        return None


def compararconcero(x):
    if x > 0:
        return "El número es mayor que 0"
    elif x < 0:
        return "El número es menor que 0"
    else:
        return "El número es igual a 0"


def operar(a, b):
    if a > b:
        return a * b
    elif a < b:
        return a / b
    else:
        return a + b


def operarnumero(n):
    if n < -5 and n > -30:
        return n + 100
    elif n >= 0 and n <= 20:
        return n + 50
    elif n > 50:
        return n * 2
    else:
        return n


def triangulo(a, b, c):
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


def alumno(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 7:
        return "Aprobado"
    elif promedio < 4:
        return "A marzo"
    else:
        return "A diciembre"


def parimpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def ordenartres(a, b, c):

    if a >= b and a >= c:
        mayor = a

        if b >= c:
            medio = b
            menor = c
        else:
            medio = c
            menor = b

    elif b >= a and b >= c:
        mayor = b

        if a >= c:
            medio = a
            menor = c
        else:
            medio = c
            menor = a

    else:
        mayor = c

        if a >= b:
            medio = a
            menor = b
        else:
            medio = b
            menor = a

    return mayor, medio, menor

