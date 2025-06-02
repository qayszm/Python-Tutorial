
#----------------------- Opjectorientierung Programmirung -----------------------
# Erstelle eine Klasse namens BankAccount
# 1- Attribute:
#         kontoinhaber (Name des Kontoinhabers)
#         kontostand (Startwert: 0.0)
# 2 - Methoden:
#         einzahlen(self, betrag): Erhöht den Kontostand um den übergebenen Betrag.
#         abheben(self, betrag): Verringert den Kontostand um den übergebenen Betrag, aber nur, wenn genug Geld vorhanden ist. Andernfalls soll eine Warnung ausgegeben werden.
#         zeige_kontostand(self): Gibt den aktuellen Kontostand aus.
# 3- Methode __str__(self) hinzu, die das Konto als lesbare Zeichenkette darstellt
# 4 - Überziehungslimit: Füge ein Attribut ueberziehungsrahmen hinzu ( -100.0 € Standardwert).
#                  Beim Abheben darf der Kontostand nicht unter das Überziehungslimit fallen.
# 5 - Zinsen berechnen: Methode zinsen_berechnen(self, zinssatz)
#            Der aktuelle Kontostand soll mit dem übergebenen Zinssatz (in %) verzinst werden, 
#            aber nur wenn der Kontostand positiv ist.


class BankAccount:
    def __init__(self, account_holder, overdraft_limit=-100.0):
        self.a_holder = account_holder
        self.a_balance = 0.0
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0:
            self.a_balance += amount
            print("Sie haben ", amount, "€ erforlgreich eingezahlt" )
        else:
            print("Der Betrag muss positve sein!")

    def withdraw(self, amount):
        if amount > 0:
            if self.a_balance - amount  >= self.overdraft_limit:
                self.a_balance -= amount
                print("Sie haben ", amount, "€ erforlgreich abgehoben" )
            else:
                print("Ihr Kontostand beträgt" , self.a_balance, "€, und die Überziehungslimit von", self.overdraft_limit, "€ würde überschritten. Vorgang nicht möglich!")
        
        else:
            print("Der Betrag muss positve sein!")

    def dispalay_account_balance(self):
        print("Ihr Aktuelle Kontostand beträgt ", self.a_balance,"€.")


    def zinsen_berechnen(self, zinssatz):
        if self.a_balance > 0:
            zinsen = self.a_balance * (zinssatz / 100)
            self.a_balance += zinsen
            print("Zinsen in Höhe von", zinsen, "€ wurden gutgeschrieben.")
        else:
            print("Keine Zinsen berechnet, da der Kontostand negativ oder null ist.")


    def __str__(self):
        return "Konto von " + self.a_holder + " - Kontostand:" +  str(self.a_balance) + "€"


account = BankAccount("Max Mustermann")
print(account)

account.deposit(200)
account.withdraw(250)
print(account)

account.withdraw(60)
print(account)

account.zinsen_berechnen(5)
print(account)
