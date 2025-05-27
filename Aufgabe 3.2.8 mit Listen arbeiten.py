
# -----------------------------  Listen [] (Array) -----------------------------

# Listen sind eine geordnete Sammlung von Elementen, die veränderbar ( hinzufügen, entfernen oder sortieren.)sind.
# Listen werden in eckigen Klammern [] definiert und die Elemente werden durch Kommas getrennt.
# Eine Liste kann leer sein oder mehrere Elemente enthalten, gemischte Datentypen enthalten, z. B. Zahlen, Strings und andere Listen.
# Listen sind nullbasiert, d. h. der Index des ersten Elements ist 0, der Index des zweiten Elements ist 1 usw.

names = ["Qays", "kais", "Manssour", 4, 7.5, True, [1, "ABC"]]

print(type(names))  # Gibt den Datentyp der Liste aus    <class 'list'>

print(names)  # Gibt die Liste aus: ["Qays", "kais", "Manssour", 4, 7.5, True]

print(names[0])  # Gibt das erste Element (Index = 0) der Liste aus: "Qays" 
print(names[2])  # Gibt das dritte Element (Index = 2) der Liste aus: "Manssour"
print(names[-1])  # Gibt das letzte Element der Liste aus: [1, "ABC"] (negativer Index zählt von hinten)
print(names[-2])  # Gibt das vorletzte Element der Liste aus: True
print(names[-1][0])  # Gibt das erste Element der letzten Liste aus: 1
print(names[-1][1])  # Gibt das zweite Element der letzten Liste aus: "ABC"


names[0] = "Sara"  # Ändert das erste Element der Liste von "Qays" zu "Sara"
print(names)  # Gibt die geänderte Liste aus: ["Sara", "kais", "Manssour", 4, 7.5, True, [1, "ABC"]]
names.append("Tony")  # Fügt ein neues Element "Tony" am Ende der Liste hinzu
print(names)  # Gibt die Liste nach dem Hinzufügen von "Tony" aus: ["Sara", "kais", "Manssour", 4, 7.5, True, [1, "ABC"], "Tony"]

# names.remove("kais")  # Entfernt das Element "kais" aus der Liste

print(names[1:4])  # Gibt die Elemente von Index 1 bis 3 (nicht inklusive 4) aus: ["kais", "Manssour", 4]
print(names[1:])  # Gibt alle Elemente ab Index 1 aus: ["kais", "Manssour", 4, 7.5, True, [1, "ABC"], "Tony"]
print(names[:3])  # Gibt die ersten drei Elemente der Liste aus: ["Sara", "kais", "Manssour"]


# -----------------------------  Aufgabe 3.2.8 mit Listen arbeiten -----------------------------

# 1- Eine Liste von Zahlen enthält, z. B. zahlen = [4, 7, 2, 9, 1, 5, 3]

numbers = [4, 7, 2, 9, 1, 5, 3]


# 2 - Gibt die Länge der Liste aus.

print("Länge der Liste:", len(numbers))  # Length Gibt die Länge der Liste aus: 7 (Elementezahl)

#-----------------------------------------------

# 3- Gibt die größte und die kleinste Zahl aus.

print("Größte Zahl:", max(numbers))  # Gibt die größte Zahl aus: 9

print("Kleinste Zahl:", min(numbers))  # Gibt die kleinste Zahl aus: 1

#-----------------------------------------------

# 4 - Berechnet den Durchschnitt (Mittelwert) der Zahlen.

average = sum(numbers) / len(numbers)  # Summe der Zahlen geteilt durch die Anzahl der Zahlen

print("Durchschnitt (Mittelwert):", average)  # Gibt den Durchschnitt der Zahlen aus: 4.428571428571429

print("Durchschnitt (Mittelwert):", round(average, 2))  # Gibt den Durchschnitt der Zahlen auf 2 Dezimalstellen gerundet aus: 4.43

#-----------------------------------------------

# 5 - Gibt die Liste in umgekehrter Reihenfolge aus.

reversed_numbers1 = numbers[::-1]  
# Umgekehrte Liste erstellen numbers[start:stop:step], 
# start (leer) = Anfang der Liste, stop (leer) = bis zum Ende, step = -1 = Schrittweise rückwärts gehen


reversed_numbers2 = list(reversed(numbers))

print("Liste in umgekehrter Reihenfolge (Methode 1):", reversed_numbers1)  # Gibt die Liste in umgekehrter Reihenfolge aus: [3, 5, 1, 9, 2, 7, 4]
print("Liste in umgekehrter Reihenfolge (Methode 2):", reversed_numbers2)  # Gibt die Liste in umgekehrter Reihenfolge aus: [3, 5, 1, 9, 2, 7, 4]

#-----------------------------------------------

# 6 - Gibt eine neue Liste aus, in der nur die geraden Zahlen enthalten sind.

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Liste mit nur geraden Zahlen:", even_numbers)


#-----------------------------------------------

# 6 - Gibt eine neue Liste aus, in der nur die ungeraden Zahlen enthalten sind.

odd_numbers = odd_numbers = [num for num in numbers if num % 2 != 0]
print("Liste mit nur ungeraden Zahlen:", odd_numbers)

