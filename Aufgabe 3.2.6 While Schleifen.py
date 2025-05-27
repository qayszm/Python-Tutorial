
# while-Schleife von 1 bis 100 zählt und jede Zahl ausgibt.

i = 1

while i <= 100:
    print(i)
    i += 1


#---------------------------------------------------------------

# Schreibe ein Programm, das den Benutzer eine Zahl zwischen 1 und 100 raten lässt. 
# Das Programm gibt Hinweise, ob die Zahl zu hoch oder zu niedrig ist, und zählt, wie viele Versuche der Benutzer braucht.

# 1 Das Programm wählt eine zufällige Zahl zwischen 1 und 100.

# 2 Der Benutzer wird aufgefordert, die Zahl zu raten.

# 3 Solange der Benutzer falsch rät, bekommt er einen Hinweis und darf es erneut versuchen.

# 4 Am Ende zeigt das Programm, nach wie vielen Versuchen die richtige Zahl erraten wurde.




import random

print("***** Zahlenraten: Raten Sie eine Zahl zwischen 1 und 100 *****")


# Zufällige Zahl zwischen 1 und 100 generieren
random_number = random.randint(1, 100)

# Zähler für die Anzahl der Versuche
i = 0

while True:
    try:
        # Benutzereingabe
        print("\nVersuch Nr.", i + 1)
        print("Die Zahl ist zwischen 1 und 100.")
        user_guess = int(input("\nGeben Sie Ihre Schätzung ein: "))
        i += 1  

        if user_guess < random_number:
            print("Ihr Versuch ist niedrig! Versuchen Sie es erneut.")
        elif user_guess > random_number:
            print("Ihr Versuch ist hoch! Versuchen Sie es erneut.")
        else:
            print("Herzlichen Glückwunsch! Sie haben die Zahl", random_number, "mit", i, "Versuchen erraten.")
            break  # Schleife beenden, wenn die Zahl richtig geraten wurde
    
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl zwischen 1 und 100 ein.")




