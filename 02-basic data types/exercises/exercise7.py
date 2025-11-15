#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

mins = int(input("Introduce una cantidad de minutos:"))
hours = int(mins/60)
minutes = int(mins%60)
print(f"{mins} minutos son {hours} horas y {minutes} minutos.")