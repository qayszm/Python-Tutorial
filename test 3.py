

def frame():
    print("\n\n\t\t" + "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸\t    🏦  Bankkonto-Verwaltung 🏦   \t🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t" + "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   1️⃣   Konto anlegen\t\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   2️⃣   Konto auswählen\t\t\t  🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸   ❌  Beenden\t\t\t\t🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t" + "🔸" * 25)


def account_frame(selected_account):
    print("\n\t\t" + "🔸" * 25)
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t🔸\t  Aktionen für Konto von " + selected_account.a_holder + "\t\t🔸")
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
    print("\t\t🔸   ❌ Zurück zum Hauptmenü\t\t\t🔸")
    print("\t\t🔸\t\t\t\t\t\t🔸")
    print("\t\t" + "🔸" * 25)


class BankAccount:
    def __init__(self, account_holder, overdraft_limit=-100.0):
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
        print("\n\t\t 💰  Ihr aktueller Kontostand beträgt", self.a_balance, "€.")

    def zinsen_berechnen(self, zinssatz):
        if self.a_balance > 0:
            zinsen = self.a_balance * (zinssatz / 100)
            self.a_balance += zinsen
            print("\n\t\t 🧮  Zinsen in Höhe von", round(zinsen,2), "€ wurden gutgeschrieben.")
        else:
            print("\n\t\t ⚠️  Keine Zinsen berechnet, da der Kontostand negativ oder null ist.")

    def __str__(self):
        return "💰  Konto von " + self.a_holder + " – Kontostand: " + str(self.a_balance) + " €"


def account_actions(selected_account):
    while True:
        account_frame(selected_account)
        action = input("\n\t\t 👉  Bitte wählen Sie eine Aktion  1️⃣  ➡️  4️⃣   oder ❌ zum Zurück: ").strip().lower()

        if action == "1":  # Einzahlen
            while True:
                try:
                    amount = float(input("\n\t\t 👉  Betrag zum Einzahlen: "))
                    if amount <= 0:
                        print("\n\t\t ⚠️  Der Betrag muss größer als 0 sein!")
                        continue
                    selected_account.deposit(amount)
                    break  # raus aus der Einzahl-Schleife
                except ValueError:
                    print("\n\t\t ⛔  Bitte eine gültige Zahl eingeben!")

        elif action == "2":  # Abheben
            while True:
                try:
                    amount = float(input("\n\t\t 👉  Betrag zum Abheben: "))
                    if amount <= 0:
                        print("\n\t\t ⚠️  Der Betrag muss größer als 0 sein!")
                        continue
                    selected_account.withdraw(amount)
                    break  # raus aus der Abheb-Schleife
                except ValueError:
                    print("\n\t\t ⛔  Bitte eine gültige Zahl eingeben!")

        elif action == "3":
            selected_account.dispalay_account_balance()

        elif action == "4":
            while True:
                try:
                    interest_rate = float(input("\n\t\t 👉  Zinssatz in % eingeben: "))
                    selected_account.zinsen_berechnen(interest_rate)
                    break
                except ValueError:
                    print("\n\t\t ⛔  Bitte eine gültige Zahl eingeben!")

        elif action == "x":
            break

        else:
            print("\n\t\t ⛔  Ungültige Eingabe.")



accounts = []



while True:
    frame()
    user_input = input("\n\t\t 👉  Bitte wählen Sie eine Option 1️⃣   - 2️⃣   - ❌ : ").strip().lower()

    if user_input == "1":
        name = input("\n\t\t 👉  Geben Sie den Namen des Kontoinhabers ein: ")
        new_account = BankAccount(name)
        accounts.append(new_account)
        print("\n\t\t ✅  Konto von", name, "wurde erfolgreich angelegt.")
        account_actions(new_account)

    elif user_input == "2":
        if not accounts:
            print("\n\t\t ⚠️   Es gibt noch keine Konten. Bitte legen Sie zuerst ein Konto an.")
            continue
        print("\n\t\t 📋  Verfügbare Konten:")
        for idx, acc in enumerate(accounts):
            print("\t\t", idx + 1, ":", acc.a_holder)
        selected = input("\n\t\t 👉  Wählen Sie ein Konto (Nummer): ")
        if not selected.isdigit() or int(selected) < 1 or int(selected) > len(accounts):
            print("\n\t\t ⛔  Ungültige Auswahl!")
            continue
        selected_account = accounts[int(selected) - 1]
        account_actions(selected_account)

    elif user_input == "x":
        print("\n\t\t 👋  Programm beendet. Vielen Dank!\n\n")
        break

    else:
        print("\n\t\t ⛔  Ungültige Eingabe.")