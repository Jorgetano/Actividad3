Notas1 = int(input("Por Favor Ingresa Su Primera Nota: "))
Notas2 = int(input("Por Favor Ingresa Su Segunda Nota: "))
Notas3 = int(input("Por Favor Ingresa Su Tercera Nota: "))

SN = Notas1 + Notas2 + Notas3


PN = SN / 3

if PN < 3.0:
    print ("Usted Ha Perdido La Materia")
elif PN > 3 and PN < 5:
    print("Felicidades Usted ha Ganado la Materia")
else:
    print("Por Favor Ingrese Un Numero Valido")
