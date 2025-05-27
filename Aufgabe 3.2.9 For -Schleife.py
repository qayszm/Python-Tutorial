
# ------------------------ For -Schleife -------------------------

for number in [3, 5, 1, 9, 2, 7, 4]:
    print(number)  # Gibt jede Zahl in der Liste einzeln aus: 3, 5, 1, 9, 2, 7, 4

for element in "Ich bin String":
    print(element)  # Gibt jeden Buchstaben des Strings einzeln aus: I, c, h, ..., g

for k in range(10):
    print(k) # Gibt die Zahlen von 0 bis 9 einzeln aus: 0, 1, ..., 9 (von Null , und nicht inklusive das Ende 10)

for i in range(5, 11):
    print(i)  # Gibt die Zahlen von 1 bis 10 einzeln aus: 5, 6, ..., 10 (nicht inklusive das Ende 11)

for j in range(1, 11, 2):
    print(j)  # Gibt die ungeraden Zahlen von 1 bis 10 einzeln aus: 1, 3, 5, 7, 9 (Schrittweite von 2 , und nicht inklusive das Ende 11 )

for num in range(10, 0, -1):
    print(num)  # Gibt die Zahlen von 10 bis 1 einzeln aus: 10, 9, ..., 1 (Schrittweise rückwärts gehen, und nicht inklusive das Ende 0)





# ------------------------Aufgabe 3.2.10 For-Schleife nutzen -------------------------

# 1-  for-Schleife alle geraden Zahlen (even) von 1 bis 100 summiert (Methode 1)

S = 0
for i in range(2, 101, 2):  # Start bei 2, Ende bei 100, Schrittweite von 2 (nicht inklusive das Ende 101)
    S += i

print("Die Summe von alle geraden Zahlen von 1 bis 100 ist:", S)  # die Summe: 2550

# ----------------------------------------------------

# for-Schleife alle geraden Zahlen (even) von 1 bis 100 summiert (Methode 2 mt sum-Funktion)

even_sum = sum(i for i in range(1, 101) if i % 2 == 0)  # Summe der geraden Zahlen, Start bei 1, Ende bei 100 (nicht inklusive das Ende 101)
print("Die Summe von alle geraden Zahlen von 1 bis 100 ist:", even_sum)  # die Summe: 2550


# -----------------------------------------------------

# 2 -  Passe das Programm so an, dass es den Benutzer fragt, bis zu welcher Zahl summiert werden soll .

user_number = int(input("Geben Sie eine Zahl, Bis zu möchten Sie die geraden Zahlen summieren: "))

user_even_sum_ = 0
for i in range(2, user_number + 1, 2):  # Start bei 2, Ende bei user_number, Schrittweite von 2, (nicht inklusive das Ende => user_number + 1)
    user_even_sum_ += i

print("Die Summe von allen geraden Zahlen von 1 bis", user_number, "ist:", user_even_sum_)


# -----------------------------------------------------

# 3 - for-Schleife alle ungeraden Zahlen (odd) von 1 bis 100 summiert (Methode 3 mit Modulo %) 

odd_sum = 0

for num in range(1, 101):  # Start bei 1, Ende bei 100,(nicht inklusive das Ende 101)
    if num % 2 != 0: # or num % 2 == 1
        odd_sum += num

print("Die Summe von allen ungeraden Zahlen von 1 bis 100 ist:", odd_sum)  # die Summe: 2500

# -----------------------------------------------------

