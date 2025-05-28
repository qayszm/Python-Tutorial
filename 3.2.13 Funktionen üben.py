def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def frame():
    print("\n\t\t"+ "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸\n\t\t🔸\t" +"    " + "🌡️  Temperatur-Umrechner 🌡️\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸\n\t\t" + "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸\n\t\t🔸   1️⃣  Celsius ➡️   Fahrenheit\t\t   🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸\n\t\t🔸   2️⃣  Fahrenheit ➡️   Celsius\t\t   🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸\n\t\t🔸   ❌ Beenden\t\t\t\t\t🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸\n\t\t" + "🔸" * 25)

while True:
    frame()
    user_input = input("\n\t\t👉  Deine Wahl: ").strip().lower()

    if user_input == "x":
        print("\n\t\t👋 Programm beendet. Aufwiedersehen! 🔚")
        break

    elif user_input == "1":
        celsius = float(input("\n\t\t🌡️  Temperatur in Celsius: ").replace(",", "."))
        try:
            fahrenheit = round(celsius_to_fahrenheit(celsius), 2)
            print("\n\t\t✅", celsius, "°C entsprechen", fahrenheit, "°F")
        except ValueError:
            print("\n\t\t⚠️ Ungültige Eingabe! Bitte eine Zahl eingeben.")

    elif user_input == "2":
        fahrenheit = float(input("\n\t\t🌡️  Temperatur in Fahrenheit: ").replace(",", "."))
        try:
            celsius = round(fahrenheit_to_celsius(fahrenheit), 2)
            print("\n\t\t✅", fahrenheit, "°F entsprechen", celsius, "°C")
        except ValueError:
            print("\n\t\t⚠️ Ungültige Eingabe! Bitte eine Zahl eingeben.")

    else:
        print("\n\t\t⚠️ Ungültige Auswahl. Bitte 1, 2 oder x wählen.")