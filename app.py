Nombre = (input("Por Favor Ingrese Su Nombre"))
Notas1 = int(input("Por Favor Ingresa Su Primera Nota: "))
Notas2 = int(input("Por Favor Ingresa Su Segunda Nota: "))
Notas3 = int(input("Por Favor Ingresa Su Tercera Nota: "))

# tambien podriamos utilizar este tipo de funciones como:
# Nombre = "Juan"
# Notas1 = "3.5"
# Notas2 = "3"
# Notas3 = "4"
# # Pero Prefiero que el usuario indique los datos los cuales podemos utilizar input para eso


SN = Notas1 + Notas2 + Notas3


PN = SN / 3

if PN < 3.0:
    print ("Usted Ha Perdido La Materia")
elif PN > 3 and PN <=  5:
    print("Felicidades Usted ha Ganado la Materia")
else:
    print("Por Favor Ingrese Un Numero Valido")
