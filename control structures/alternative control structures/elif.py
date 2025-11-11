mark = int(input("Say your mark: "))
if mark >= 1 and mark <=4:
    print("suspenso")
elif mark == 5:
    print("suficiente")
elif mark == 6 or mark ==7:
    print("bien")
elif mark == 8:
    print("notable")
elif mark == 9 or mark==10:
    print("sobresaliente")
else:
    print("nota incorrecta")
print("Finished program")