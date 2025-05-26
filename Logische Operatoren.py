
# ------------------- Logische Operatoren ( AND , OR , NOT ) -------------------

# Logische Operatoren werden verwendet, um Bedingungen zu kombinieren.
# Sie geben einen booleschen Wert zurück (True oder False).



# 1- Beispiel mit Nested if-Anweisungen (Wenn eine Bedingung erfüllt ist, wird die nächste Bedingung überprüft)


print ("Willkommen zum Gewinnspiel mit Nested if Anweisungen!")

number1 = int(input("Bitte wählen eine Zahl zwischen 1 und 49: "))
number2 = int(input("Bitte wählen eine Zahl zwischen 1 und 49: "))
number3 = int(input("Bitte wählen eine Zahl zwischen 1 und 49: "))

# Gewinnzahlen 1: number1 = 3
# Gewinnzahlen 2: number2 = 14
# Gewinnzahlen 3: number3 = 22
# Wenn alle drei Zahlen übereinstimmen, hat der Spieler gewonnen.

# Überprüfen der Gewinnzahlen ein nach dem anderen

if number1 == 3:
    if number2 == 14:
        if number3 == 22:
            print("Herzlichen Glückwunsch! Sie haben gewonnen!")
        else:
            print("Leider haben Sie nicht gewonnen (erste und zweite Nummer waren richtg aber die dritte war falsch)")
    else:
        print("Leider haben Sie nicht gewonnen (erste Nummer war richtg aber die zweite war falsch) .")
else:
    print("Leider haben Sie nicht gewonnen (erste Nummer war falsch).")  


# 2- Das selbe Beispiel mit logischen Operatoren (and)

print("Willkommen zum Gewinnspiel mit logischen Operatoren!")

number4 = int(input("Bitte wählen eine Zahl zwischen 1 und 49: "))
number5 = int(input("Bitte wählen eine Zahl zwischen 1 und 49: "))
number6 = int(input("Bitte wählen eine Zahl zwischen 1 und 49: "))

# Gewinnzahlen 1: number4 = 3
# Gewinnzahlen 2: number5 = 14
# Gewinnzahlen 3: number6 = 22

# Wenn alle drei Zahlen übereinstimmen, hat der Spieler gewonnen. (AND ergibt True, wenn alle Bedingungen True sind)

if number4 == 3 and number5 == 14 and number6 == 22:
    print("Herzlichen Glückwunsch! Sie haben gewonnen!")
else:
    print("Leider haben Sie nicht gewonnen. (mindestens eine Nummer war falsch)")
