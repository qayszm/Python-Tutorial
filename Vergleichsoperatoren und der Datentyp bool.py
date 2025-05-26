
# --------------------- Vergleichsoperatoren und der Datentyp bool (False, True) ---------------------

# (<) kleiner als ,    (>) größer als
# (<=) kleiner als oder gleich ,    (>=) größer als oder gleich
# (==) Gleich Operator,    (!=) ungleich




print(5 < 1)  # Ausgabe: False, da 5 nicht kleiner als 1 ist
print(5 > 1)  # Ausgabe: True, da 5 größer als 1 ist 
print(5 >= 5)  # Ausgabe: True, da 5 größer oder gleich 5 ist
print(5 <= 5)  # Ausgabe: True, da 5 kleiner oder gleich 5 ist
print(5 == 5)  # Ausgabe: True, da 5 gleich 5 ist
print(5 != 1)  # Ausgabe: True, da 5 ungleich 1 ist
print(4 != 1)  # Ausgabe: True, da 4 ungleich 1 ist
print((4 + 2) * 3 == 5)  # Ausgabe: False, da 18 nicht gleich 5 ist


#-------------------------der Datentyp bool (False, True)-------------------------


print(type(5 < 1))  # Ausgabe: <class 'bool'>, boolescher / boolian (False, True) Wert