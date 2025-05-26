
# ------------------------- type() Funktion -----------------------

value1 = input("Erste Zahl: ")
value2 = input("Zweite Zahl: ")

print("Addition ist :")
print(value1 + value2)  

#Erste Zahl = 2
#Zweite Zahl = 3
#Ergebnis = 23 (Falsche Addition, da beide Werte als Strings behandelt werden und verkettet werden)

type_of_value1 = type(value1)  # Gibt den Data-Typ von value1 zurück, der hier 'str' ist
type_of_value2 = type(value2)  # Gibt den Data-Typ von value2 zurück, der hier 'str' ist

print("Typ von value1:", type_of_value1)
print("Typ von value2:", type_of_value2)

# *****  Mit input() Funktion werden die Werte als Strings eingelesen/gespeichert *****



# ------------------------   Type-Casting-Funktionen ------------------------

# 1- int() Funktion wandelt den String in eine Ganzzahl/Integer um

print("Addition ist:")
print(int(value1) + int(value2))

#Ergebnis = 5 (die Addition ist korrekt, da die Strings in Ganzzahlen umgewandelt wurden)



# Beispiel für die Umwandlung von String zu Integer mit input()
# *** Die Eingabe muss nur Ganzzahlen / Integer ohne komma (.) /Float enthalten, sonst gibt es einen Fehler ***

value3 = int(input("Dritte Zahl: "))
value4 = int(input("Vierte Zahl: "))

print("Addition-2 ist:")
print(value3 + value4)


# 2- float() Funktion wandelt den String in eine Fließkommazahl/Float um
# *** Die Eingabe darf nur Ganzzahlen / Integer oder Fließkommazahl/Float mit Komma (.) enthalten

value5 = float(input("Fünfte Zahl: "))
value6 = float(input("Sechste Zahl: "))

print("Addition-3 ist:")
print(value5 + value6)