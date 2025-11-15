"""
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
"""

sueldo_base=1200.0
venta1=230
venta2=58
venta3=156
comision = (venta1*0.1)+(venta2*0.1)+(venta3*0.1)
sueldo_mes = sueldo_base+comision
print(f"El sueldo que va a recibir este mes será: {sueldo_mes}")
