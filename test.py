
def frame():
    print("\n\t\t" + "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸\t    🏦  Bankkonto-Verwaltung 🏦   \t🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t" + "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   1️⃣  Einzahlen\t\t\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   2️⃣  Abheben\t\t\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   3️⃣  Kontostand anzeigen\t\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   4️⃣  Zinsen berechnen\t\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   ❌ Beenden\t\t\t\t\t🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t" + "🔸" * 25)


class BankAccount:
    def __init__(self, account_holder, overdraft_limit = -100.0):
        self.a_holder = account_holder
        self.a_balance = 0.0
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.a_balance += amount
            print("\n\t\t ✅  Sie haben", amount, "€ erfolgreich eingezahlt. 💵")
        else:
            print("\n\t\t ⚠️  Der Betrag muss positiv sein!")

    def withdraw(self, amount):
        if amount > 0:
            if self.a_balance - amount >= self.overdraft_limit:
                self.a_balance -= amount
                print("\n\t\t ✅  Sie haben", amount, "€ erfolgreich abgehoben. 💸")
            else:
                print("\n\t\t 🔒  Ihr Kontostand beträgt", self.a_balance, "€, Überziehungsrahmen von", self.overdraft_limit, "€ überschritten.")
        else:
            print("\n\t\t ⚠️  Der Betrag muss positiv sein!")

    def dispalay_account_balance(self):
        print("💰  Ihr aktueller Kontostand beträgt", self.a_balance, "€.")

    def zinsen_berechnen(self, zinssatz):
        if self.a_balance > 0:
            zinsen = self.a_balance * (zinssatz / 100)
            self.a_balance += zinsen
            print("\n\t\t 🧮  Zinsen in Höhe von", zinsen, "€ wurden gutgeschrieben.")
        else:
            print("\n\t\t ⚠️  Keine Zinsen berechnet, da der Kontostand negativ oder null ist.")

    def __str__(self):
        return "💰  Konto von " + self.a_holder + " – Kontostand: " + str(self.a_balance) + " €"


name = input("\n\n\t\t 👉  Geben Sie den Namen des Kontoinhabers ein: ")

account = BankAccount(name)

while True:
    frame()
    user_input = input("\n\t\t 👉  Bitte wählen Sie eine Option (1-4) oder X zu beenden: ").strip().lower()

    if user_input == "1":
        amount = float(input("\n\t\t 👉  Bitte geben Sie einen Betrag zum Einzahlen ein: "))
        account.deposit(amount)

    elif user_input == "2":
        amount = float(input("\n\t\t 👉  Bitte geben Sie einen Betrag zum Abheben ein: "))
        account.withdraw(amount)

    elif user_input == "3":
        print(account)

    elif user_input == "4":
        zinssatz = float(input("\n\t\t 👉  Bitte geben Sie ein Zinssatz in % zum Berechnen: "))
        account.zinsen_berechnen(zinssatz)

    elif user_input == "x":
        print("\n\t\t 👉  Programm beendet. Vielen Dank!")
        break

    else:
        print("\n\t\t ⚠️  Ungültige Eingabe. Bitte wählen Sie eine Zahl von 1 bis 4 oder X zu beenden.")



