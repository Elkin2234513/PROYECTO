#REGLA DEL 50 30 20
def REGLA503020(Sueldo):

    if Sueldo > 1300606:
        Gastos_basicos = Sueldo*0.5
        GASTOS_EXTRA = Sueldo*0.3
        AHORRO = Sueldo*0.2
        print("PARA GASTOS BASICOS NECESITAS= " +str(Gastos_basicos))
        print("PARA LUJOS Y COSAS EXTRAS DISPONES DE= " + str(GASTOS_EXTRA))
        print("PARA AHORRAR TE QUEDA= " + str(AHORRO))

    else:
      print("LO SIENTO NO TE ALCANZA")

Sueldo = int(input("DIGITE SU SUELDO: "))

REGLA503020(Sueldo)

#REGLA DEL 60 10 10 20 
def REGLA60101020(Sueldo):
    if Sueldo > 1300606:
       Gasto_basicos = Sueldo*0.6
       AHORROS = Sueldo*0.1
       INVERTIR = Sueldo*0.1
       GASTOS_EXTRA = Sueldo*0.2
       print("PARA GASTOS BASICOS NECESITAS= " +str(Gasto_basicos))
       print("PARA AHORRAR TE QUEDA= "+ str(AHORROS))
       print("PARA INVERTIR= "+ str(INVERTIR))
       print("PARA GASTOS EXTRAS TE QUEDO= "+ str(GASTOS_EXTRA))
    else:
       print("LO SIENTO NO TE ALCANZA")
       
Sueldo = int(input("DIGITE SU SUELDO: "))

REGLA60101020(Sueldo)