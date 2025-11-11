# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for table in range(1,6):
    for num in range(0,11):
        print("%d * %d = %d" % (num, table, num*table))