

# Kummentar in Python mit # Zeichen (Hash, Raute)


#-------------------- Print() Funktion -------------------
# print() Funktion wird verwendet, um Daten auf dem Bildschirm auszugeben

print("Hallo Welt")




#------------------- Zahlen in Pyhton ----------------------

# 1 Ganze Zahlen (Positive + und Negative -)
print(-7, 4, 0, 3460000000)

#       - Addition (plusrechnnung)          +  Zeichen
print(7 + 4)

#       - Subtraktion (minusrechnnung)      -  Zeichen
print(7 - 4)

#       - Multiplikation (malrechnnung)     *  Zeichen
print(7 * 4)

#       - Division (durchrechnnung)         /  Zeichen
print(8 / 4)


print(3 + 2 * 2 - 1)
print((3 + 2) * (2 - 1))

# 2 Fließkommazahlen (Kommazahlen)  Komma In Python ist Punkt (.)
print(2.1 + 1.5)
print(2.4 * 2)




#--------------------- Text in Pyhton -------------------

# 2 Strings (Text)  Text in Python ist immer in Anführungszeichen "" oder ''
print("Hallo Welt")
print('Hallo Welt')

#        "" und  '' zusmmmen 
print('Die Programmiersprache "Python" ist cool')
print("Die Programmiersprache 'Python' ist cool")

#        Mehrzeilige Strings (Text) zwischen 3 Anführungszeichen """   """ oder '''  '''
print('''Die 
      Programmiersprache "Python" ist cool''')

print("""Die
      Programmiersprache "Python" ist cool""")

print('''Die
      Programmiersprache "Python" ist cool''')

print('''Die
      Programmiersprache 'Python' ist cool''')

#       Sring's Verketten mit ( + ) Zeichen
print("Hallo" + "Welt")
print("Hallo " + "Welt")
print("Hallo" + " " + "Welt")





#---------------------- Variablen --------------------

# Variablen sind Datenbehälter für Werte, wurden mit Bezeichner(Name) definiert
# Variablen wurden mit (=) Zeichen definiert
# Variablen darf nur ein Wert behalten (nach den Daten-Typen)

# Tips für Wahl des Variablen-Bezeichners (Name):
# 1- Sprechend bennen, besser auf englische begriffe
# 2- Variablen Namen sind immer klein geschrieben
# 3- Variablen Namen sind immer mit Buchstaben (a-z) oder (A-Z) und _ (Unterstrich) beginnend
# 4- Variablen Namen sind immer mit Buchstaben (a-z) oder (A-Z) und _ (Unterstrich) und Zahlen (0-9) fortgesetzt
# 5- Variablen Namen sind immer ohne Leerzeichen
# 6- Variablen Namen sind immer ohne Sonderzeichen (z.B. @, #, $, %, &, *, !, ?, /, \, +, -, =, <, >) oder Umlaute (ä, ö, ü)
# 8- Variablen Namen sind immer ohne reservierte Wörter (z.B. if, else, for, while, def, class, import, from, as, try, except, finally, with, in, is, and, or, not)
# 9- Variablen Namen sind immer ohne Schlüsselwörter (z.B. True, False, None, self, super, global, nonlocal, lambda, yield, async, await)
# 10- Snake case Benennen-Type wrde mit Python vewendet => Variablen Namen sind immer mit _ (Unterstrich) getrennt (z.B first_name)




age = 27
name = "Qays"
print(age)
print(name)

# eine vorgegbene Variable mit einem neuen Wert zuweisen
age = 28
print(age)
print(name)



#--------------------- Datentypen (int, float und str) ---------------------

# 1- int => Integer  für Ganzzahlen  Positive + oder Negative - oder 0

int_variable = 100
print(int_variable)

# 2- float => Fließkommazahl (Kommazahlen) Komma in Python ist Punkt (.)

float_variable = 13.734
print(float_variable)

# 3- str => String für Text, immer in Anführungszeichen "" oder ''

str_variable1 = "Das ist ein String"
str_variable2 = 'Das ist ein String'

print(str_variable1)
print(str_variable2)
