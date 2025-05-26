
#Erstelle ein Programm das einen Datensatz zum Thema Zimmer mit 10 Eigenschaften einlesen kann
# und die Daten wieder geschlossen ausgeben kann.

room_number = input("Zimmernummer: ")
room_type = input("Zimmertyp (z.B. Schlafzimmer, Wohnzimmer): ")
size = input("Fläche in qm: ")
floor = input("Etage: ")
window_count = input("Fensteranzhal: ")
color = input("Farbe der Wände: ")
balcony = input("Balkon (ja/nein): ")
air_condition = input("Klimaanlage (ja/nein): ")
wifi = input("WiFi (ja/nein): ")
tv = input("Fernseher (ja/nein): ")

print("Zimmernummer:", room_number)
print("Zimmertyp:", room_type)
print("Fläche in qm:", size)
print("Etage:", floor)
print("Fensteranzahl:", window_count)
print("Farbe der Wände:", color)
print("Balkon:", balcony)
print("Klimaanlage:", air_condition)
print("WiFi:", wifi)
print("Fernseher:", tv)
