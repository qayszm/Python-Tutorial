
# ---------------- Die if Anweisung ----------------
# Die if-Anweisung wird verwendet, um  zu überprüfen und Code nur auszuführen, wenn die Bedingung wahr ist.

age = int(input("Geben Sie Ihr Alter ein: "))

if age < 18:
    print("Achtung, der Nutzer minderjährig.")
    print("ich bin immer noch innerhalb if-Anweisung / if-Block.")
elif age == 18:
    print("Der Nutzer ist genau 18 Jahre alt.") 
elif age == 19:
    print("Der Nutzer ist genau 19 Jahre alt.") 
else:
    print("Der Nutzer ist volljährig.")

print("ich bin außererhalb if-Anweisung / if-Block. _ Neue Zeile / Code wird immer ausgeführt.")

# Bedingung ist True, Wenn das Alter kleiner als 18 ist
# der Code innerhalb des if-Blocks (nach Rückung / TAB) wird ausgeführt, wenn die Bedingung wahr / True ist.
# Wenn die Bedingung ( von if ) nicht wahr / False ist, wird die elif-Anweisung überprüft.
# ( mehrere Bedingung hinzufügen ) Wenn die elif-Bedingung wahr / True ist, wird der Code innerhalb des elif-Blocks ausgeführt.
# Wenn alle Bedingungen (if , elif) nicht wahr / False sind, wird der Code innerhalb des else-Block (nach Rückung / TAB) ausgeführt.

# Der Code außerhalb der if-Anweisung wird immer ausgeführt, unabhängig von der Bedingung.