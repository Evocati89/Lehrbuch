#Spiel zum Lehrbuch - Python
#2 Zahlen berechnen und das Ergebnis dem Programm mitteilen. Dieses prüft auf Richtigkeit

#include
import random
random.seed()

#Var defination
ranA = random.randint(1,10)
ranB = random.randint(1,10)

#calc
result = ranA + ranB

#User communication
print(f"Bitte berechnen Sie {ranA} + {ranB}",
      "\nGeben Sie das Ergebnis hier ein: ")
userResult = int(input())

if userResult == result:
      print(f"Das eingegebene Ergebnis {userResult} ist richtig!")
else:
      print(f"Das eingegebene Ergebnis {userResult} ist falsch!\n",
            f"Das richtige Ergbebnis lautet: {result}")


