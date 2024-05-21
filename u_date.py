#Exercise Date
#Input
print(f"Bitte geben Sie das Datum ein\nTag:")
iDay = int(input())
print(f"Monat:")
iMonth = int(input())
print(f"Jahr:")
iYear = int(input())

#Examination Day and Month
if iDay > 31 or iDay < 1:
    print(f"Der Tag ist ungültig!")
elif iMonth > 12 or iMonth < 1:
    print(f"Der Monat ist ungültig!")

#Last day of Month
if iMonth == 1 or iMonth == 3 or iMonth == 5 or iMonth == 7 or iMonth == 8 or iMonth == 10 or iMonth == 12:
    print(f"Der letzte Tag des Monats ist: 31")
    iLastDay = 31
elif iMonth == 2:
    print(f"Der letzte Tag des Monats ist: 28")
    iLastDay = 28
elif iMonth == 4 or iMonth == 6 or iMonth == 9 or iMonth == 11:
    print(f"Der letzte Tag des Monats ist: 30")
    iLastDay = 30

#Examination Day
if iDay < 1:
    print("Der eingegebene Tag ist kleiner als 1")
elif iDay > iLastDay:
    print("Der eingegebene Tag ist größer als der letzte Tag des Monats")

#Examination Year
iExYear = iYear // 4
type(iExYear)