# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

day = int(input("Input a day: "))
month = int(input("Input a month: "))
year = int(input("Input a year: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days_month = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days_month = 30
elif month == 2:
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        days_month = 29
    else:
        days_month=28

else:
    print("Incorrect date")
    
if day < 0 or day > days_month:
    print("Incorrect date")
else:
    print("Correct date")