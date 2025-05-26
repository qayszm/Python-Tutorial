
# ---------------------- IF-Übungen ----------------------

# 1- Ist die Zahl vom Benutzer Gerade oder ungerade?

print("\n\n***** Gerade oder ungerade *****\n")

number1 = int(input("Geben Sie eine ganze Zahl ein: "))

if number1 == 0:
    print("\nDie Zahl ist null.")
elif number1 % 2 == 0:
    print("\nDie Zahl ist gerade.")
else:
    print("\nDie Zahl ist ungerade.")

print("\n-------------------------------\n")


#-----------------------------------------------------------------------------------

# 2- Ist die Zahl vom Benutzer Positiv, negativ oder null?

print("***** Positiv, negativ oder null *****\n")

number2 = float(input("Geben Sie eine Zahl ein: ")) # ganzzahl oder Kommazahl

if number2 > 0:
    print("\nDie Zahl ist positiv.")
elif number2 < 0:
    print("\nDie Zahl ist negativ.")
else:
    print("\nDie Zahl ist null.")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 3- Passwort prüfen

# Richtiges Passwört = "geheim"

print("***** Passwort prüfen *****\n")

password = input("Geben Sie Ihr Passwort ein: ")

if password == "geheim":
    print("\nRichtiges Passwört. Willkommen!")
else:
    print("\nFalsches Passwort. Versuchen Sie es erneut.")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 4 - Schul-Notenbewertung, Zahl zwischen 1 und 6 (z. B. 1 = sehr gut, 6 = ungenügend )


print("***** Notenbewertung *****\n")

note = int(input("Geben Sie eine Zahl zwischen 1 und 6 ein: "))

if note == 1:
    print("\nSehr gut!")
elif note == 2:
    print("\nGut!")
elif note == 3:
    print("\nBefriedigend!")
elif note == 4:
    print("\nAusreichend!")
elif note == 5:
    print("\nMangelhaft!")
elif note == 6:
    print("\nUngenügend!")
else:
    print("\nUngültige Note. Bitte geben Sie eine Zahl zwischen 1 und 6 ein.")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 4- Größte von drei Zahlen

print("***** Größte von drei Zahlen *****\n")

num1 = float(input("Geben Sie die erste Zahl ein: "))
num2 = float(input("Geben Sie die zweite Zahl ein: ")) 
num3 = float(input("Geben Sie die dritte Zahl ein: "))

maximum = num1 if num1 > num2 else num2
maximum = maximum if maximum > num3 else num3

if num1 == num2 == num3:
    print("\nAlle drei Zahlen sind gleich.")
else:
    print("\nDie größte Zahl ist: ", maximum)

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 5- Schaltjahr-Prüfung (durch 4 teilbar, aber nicht durch 100, außer es ist durch 400 teilbar)

print("***** Schaltjahr-Prüfung *****\n")

year = int(input("Geben Sie ein Jahr ein: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("\nDas Jahr", year, "ist ein Schaltjahr.")
else:
    print("\nDas Jahr", year, "ist kein Schaltjahr.")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 6- Überprüfe, ob die zweite Zahl zwischen der ersten und dritten liegt.

print("***** Ist die zweite Zahl liegt zwischen der ersten und dritten *****\n")

num4 = float(input("Geben Sie die erste Zahl ein: "))
num5 = float(input("Geben Sie die zweite Zahl ein: "))
num6 = float(input("Geben Sie die dritte Zahl ein: "))

if num4 == num5 == num6:
    print("\nAlle drei Zahlen sind gleich.")
elif (num4 < num5 < num6) or (num4 > num5 > num6):
    print("\nDie zweite Zahl (", num5, ") liegt zwischen dem ersten Zahl (", num4, ") und dem dritten Zahl (", num6, ").")
else:
    print("\nDie zweite Zahl (", num5, ") liegt nicht zwischen dem erstenZahl (", num4, ") und dem dritten Zahl (", num6, ").")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 7- Rabatt-Rechner (Wenn der Einkaufswert über 100 € liegt, gibt es 10 % Rabatt)

print("***** Endpreis *****\n")

payments = float(input("Geben Sie den Einkaufswert in Euro ein: "))

if payments > 100:
    end_price = payments * 0.90  # 10% Rabatt
    print("\nGlückwunsch!! Sie bekommen 10% Rabatt!")
else:
    end_price = payments
    print("\nLeider, Sie bekommen keinen Rabatt. Ab Einkaufswert über 100€ gibt es 10% Rabatt.")

print("\nDer Endpreis beträgt: ", end_price, "€")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 8- Ampelsystem (rot, gelb, grün) und gib aus, was man machen soll (z. B. "stehen bleiben", "bereit machen", "gehen").

print("***** Ampelsystem *****\n")

traffic_light = input("Geben Sie die Ampelfarbe ein (rot, gelb, grün): ").lower()

if traffic_light == "rot":
    print("\nStehen bleiben!")
elif traffic_light == "gelb":
    print("\nBereit machen!")
elif traffic_light == "grün":
    print("\nGehen!")
else:
    print("\nUngültige Ampelfarbe. Bitte geben Sie rot, gelb oder grün ein.")

print("\n-------------------------------\n")

#-----------------------------------------------------------------------------------

# 9- BMI-Rechner mit Bewertung (Gewicht / Größe^2)


print("***** BMI-Rechner *****")

# Gewicht Eingabe , Ersetzt Komma (,) durch Punkt (.)

while True:
    try:
        weight_str = input("\nBitte geben Sie Ihr Gewicht in Kilogramm ein (z.B. 70.5): ")
        weight = float(weight_str.replace(',', '.'))
        if weight <= 0 or weight > 200:
            print("\nDas Gewicht muss ein positiver Wert in Kilogramm sein (z.B. 70.5).")
            continue
        break
    except ValueError:
        print("\nUngültige Eingabe. Bitte geben Sie eine Zahl für das Gewicht ein.")

# # Größe Eingabe , Ersetzt Komma (,) durch Punkt (.)
while True:
    try:
        height_str = input("\nBitte geben Sie Ihre Größe in Metern ein (z.B. 1.75): ")
        height = float(height_str.replace(',', '.'))
        if height <= 0 or height > 2.5:
            print("\nDie Größe muss ein positiver Wert in Metern sein (z.B. 1.75).")
            continue
        break
    except ValueError:
        print("\nUngültige Eingabe. Bitte geben Sie eine Zahl für die Größe ein.")

bmi = weight / (height ** 2)
print("\nIhr BMI ist: ", round(bmi, 2))


if bmi < 18.5:
    category = "Untergewicht"
elif 18.5 <= bmi < 25:
    category = "Normalgewicht"
elif 25 <= bmi < 30:
    category = "Übergewicht"
elif 30 <= bmi < 40:
    category = "Adipositas"
else:
    category = "extreme Adipositas" # BMI >= 40
  

print("Bewertung: ", category)

print("\n-------------------------------\n")
#-----------------------------------------------------------------------------------

# 10 - Multiple Choice Bewertung (Benutzer-Antwort (A, B, C oder D) auf eine Frage. 
# Überprüfe, ob sie korrekt ist (z. B. C) und gib „richtig“ oder „falsch“ aus.)

print("***** Multiple Choice Bewertung *****\n")

question = "Was ist die Hauptstadt von Deutschland?\n\nA) München \nB) Frankfurt \nC) Berlin \nD) Hamburg\n"

user_answer = input(question + "\nGeben Sie Ihre Antwort (A, B, C oder D) ein: ").upper()

correct_answer = "C"

if user_answer == correct_answer:
    print("Richtig!")
else:
    print("Falsch! Die richtige Antwort ist:", correct_answer)
