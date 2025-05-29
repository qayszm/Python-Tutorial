
#-------------------------------------------------------------------------
# --                 Objektorientierung  Programmierung OOP             --
# ------------------------------------------------------------------------

# Objektorientierung ist ein Programmierparadigma, das auf der Verwendung von Objekten basiert.
# Ein Objekt ist eine Instanz einer Klasse, die Daten (Attribute) und Funktionen (Methoden) kapselt.
# Eine Klasse ist ein Bauplan für Objekte, der die Struktur und das Verhalten definiert.
# In Python wird die Objektorientierung durch die Verwendung von Klassen und Objekten implementiert.
# Eine Klasse wird mit dem Schlüsselwort "class" definiert, gefolgt vom Klassennamen (Pascal case style Z.B. ClassName) und einem Doppelpunkt.
# Eine Klasse kann Attribute (Variablen) und Methoden (Funktionen) enthalten.
# Attribute sind Variablen, die den Zustand eines Objekts beschreiben, und Methoden sind Funktionen, die das Verhalten eines Objekts definieren.
# def ist eine spezielle Methode, die den Konstruktor der Klasse darstellt und beim Erstellen eines Objekts aufgerufen wird.
# __intit__  "initialisieren" ist eine spezielle Methode (Dunder or Magic Method), die den Konstruktor der Klasse darstellt und beim Erstellen eines Objekts automatisch aufgerufen wird.
# __init__ wird verwendet, um die Attribute des Objekts zu initialisieren.
# __init_ nimmt Parameter entgegen, die beim Erstellen eines Objekts übergeben werden, und weist sie den Attributen des Objekts zu.
# self ist ein Verweis auf das aktuelle Objekt und wird verwendet, um auf die Attribute und Methoden der Klasse zuzugreifen.
# self muss immer als erstes Argument in Methoden der Klasse verwendet werden, um auf die Instanzattribute zuzugreifen.
# Pyton unterstützt Vererbung, d. h. eine Klasse kann von einer anderen Klasse erben und deren Attribute und Methoden erweitern oder überschreiben.

# Syntax für die Definition einer Klasse:
# class ClassName:
#   def __init__(self, attribute1, attribute2):              # Konstruktor der Klasse
#       self.attribute_name1(attribute1) = attribute1        # Konstruktor-Parameter, die beim Erstellen eines Objekts übergeben werden
#       self.attribute_name2(attribute2) = attribute2

#   def method_name(self, parameter1, parameter2):           # Methode der Klasse
#         Code der Methode
#         return value                                       # Optional: Rückgabewert der Methode



class Car:                          # Definition der Klasse Car
    def __init__(self):             # Konstruktor der Klasse Car
        self.car_brand = None       # Attributeinitialisieren
        self.horse_power = None
        self.color = None

print(type(Car))  # Gibt den Datentyp der Klasse Car aus: <class 'type'>

print(dir(Car))  # Gibt die Attribute und Methoden der Klasse Car aus


#------------------------------

car1 = Car()     # Objekt/Instanz  Erstellen  von calss Car

print(car1.car_brand)  # Gibt den Wert des Attributs car_brand des Objekts car1 aus (aktuell None)


car1.car_brand = "Audi"  # Setzt den Wert des Attributs car_brand des Objekts car1 auf "Audi"
car1.horse_power = 250
car1.color = "Blau"

print(car1.car_brand)              #  "Audi"
print(car1.horse_power)            #  250
print(car1.color)                  #  "Blau"


print (type(car1))   # Gibt den Datentyp des Objekts car1 aus: <class '__main__.Car'>

print(dir(car1))     # Gibt die Attribute und Methoden des Objekts car1 aus


#------------------------------

car2 = Car()     # Objekt/Instanz  Erstellen  von calss Car

car2.car_brand = "BMW"  # Setzt den Wert des Attributs car_brand des Objekts car1 auf "Audi"
car2.horse_power = 150
car2.color = "Schwarz"

print(car2.car_brand)              #  "BMW" 
print(car2.horse_power)            #  150
print(car2.color)                  #  "Schwarz"


#------------------------------

# die Repräsentation des Objekts . 
# Die Nummer am Ende ist Referenz/Link zu der Adresse des Objekts im Speicher/RAM
# Es wurde die Attibute und Methoden (Werte) eines Objekts gespeichert.

print(car1)          # <__main__.Car object at 0x000002408F946A50>
print(car2)          # <__main__.Car object at 0x0000019399CB8A50>

car3 = car1  # car3 ist eine Referenz auf das gleiche Objekt (die selbe Werte) wie car1 in dem Speicher => car1 und car3 zeigen auf dasselbe Objekt in Speicher

print(car3)          # <__main__.Car object at 0x000002408F946A50> 

# car3 zeigt auf dasselbe Objekt wie car1

print(car1 is car3)  # Gibt True zurück, da car3 und car1 auf dasselbe Objekt verweisen

print(car1.car_brand)              #  "Audi"
print(car3.car_brand)              #  "Audi"

car3.car_brand = "Mercedes"  # Ändert den Wert des Attributs car_brand des Objekts car3 (und damit auch car1, da sie auf dasselbe Objekt verweisen)

print(car1.car_brand)              #  "Mercedes"
print(car3.car_brand)              #  "Mercedes"


print(car1 is car2)  # Gibt False zurück, da car1 und car2 auf verschiedene Objekte verweisen


#------------------------------Methode hinzufügen----------------

class CarInStore:                          # Definition der Klasse CarInStore
    def __init__(self, car_brand, horse_power, color):  # Konstruktor der Klasse Car
        self.car_brand = car_brand  # Attribute initialisieren
        self.horse_power = horse_power
        self.color = color

    def display_info(self):  # Methode zur Anzeige der Informationen des Autos
        return f"Marke: {self.car_brand}, PS: {self.horse_power}, Farbe: {self.color}"
    

car3 = CarInStore("Audi", 250, "Blau")  # Objekt/Instanz erstellen von class Car

car3.display_info()  # Aufruf der Methode display_info des Objekts car3

print(car3.display_info())  # Gibt die Informationen des Autos aus: Marke: Audi, PS: 250, Farbe: Blau


# ------------------------------------

class CarRace:                          # Definition der Klasse CarRace
    def __init__(self, car_brand, horse_power, color):       # Konstruktor der Klasse Car
        self.car_brand = car_brand                            # Attribute initialisieren
        self.horse_power = horse_power
        self.color = color
        self.x_position = 0                        # Initialisiert die Position auf x-Achse des Autos auf 0
        self.y_position = 0                       # Initialisiert die Position auf y-Achse des Autos auf 0

    def drive(self, x, y) #:  # Methode zum Fahren des Autos
        self.x_position += x  # Aktualisiert die x-Position des Autos
        self.y_position += y  # Aktualisiert die y-Position des Autos

    
car_a = CarRace("Audi", 250, "Blau")  # Objekt/Instanz erstellen von class CarRace

print(car_a.x_position)  # Gibt die aktuelle x-Position des Autos aus: 0
print(car_a.y_position)  # Gibt die aktuelle y-Position des Autos aus: 0

car_a.drive(10, 5)  # Fährt das Auto um 10 Einheiten in x-Achse und 5 Einheiten in y-Achse

print(car_a.x_position)  # Gibt die aktualisierte x-Position des Autos aus: 10
print(car_a.y_position)  # Gibt die aktualisierte y-Position des Autos aus: 5


 