cal1 = 6
cal2 =7
cal3 = 8
promedio_parciales = ((cal1+cal2+cal3)/3)*0.55
examen_final = 5
promedio_examen = examen_final*0.3
trabajo_final = 8
promedio_trabajo_final = trabajo_final * 0.15

nota_final = promedio_parciales + promedio_examen + promedio_trabajo_final
print(f"La nota final es de: {round(nota_final, 2)}")