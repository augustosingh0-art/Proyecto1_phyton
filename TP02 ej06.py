persona = str(input(f"Ingrese su nombre y apellido: "))
cargo = str(input(f"Ingrese su cargo(empleado,administrativo o gerente): "))
if cargo == "empleado" :
     sueldo = 600000
elif cargo == "administrativo" :
     sueldo = 800000
elif cargo == "gerente" :
    sueldo = 1000000
else: 
    print("Cargo no valido")
    sueldo = 0

if sueldo > 0 :
     bonus = input("¿Usted posee un bonus por presentismo?")
     if bonus == "si":
          sueldo = sueldo * 1.15 #15%
     else:
          sueldo = sueldo * 0.95 #-5%

print(f"El monto a percibir es: ${sueldo}")