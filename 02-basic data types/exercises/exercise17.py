# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
horas = int(input("Introduce la hora a la que salió el ciclista:"))
minutos = int(input("Introduce los minutos a los que salio el ciclista:"))
segundos = int(input("Introduce los segundos a los que salió el ciclista:"))
segviaje = int(input("Introduce el tiempo que ha tardado en segundos:"))

seginicial = horas*3600+minutos*60+segundos
segtotales = seginicial + segviaje
horallegada = (segtotales//3600)
minllegada =  (segtotales%3600)//60
segllegada = (segtotales % 3600)%60

print(f"Hora de llegada {horallegada}:{minllegada}:{segllegada}")