#Exercise Date
#Input
print(f"Bitte geben Sie das Datum ein\nTag:")
iDay = int(input())
print(f"Monat:")
iMonth = int(input())
print(f"Jahr:")
iYear = int(input())

#Examination
if iDay > 31 or iDay < 1:
    print(f"Der Tag ist ungültig!")
elif iMonth > 12 or iMonth < 1:
    print(f"Der Monat ist ungültig!")


