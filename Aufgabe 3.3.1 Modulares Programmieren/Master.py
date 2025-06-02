from Frames import *

from BankAccountClass  import BankAccount



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