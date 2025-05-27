
# Benutzer kann so lange Zahlen eingeben, bis er stop eingibt. 
# Verwende eine while-Schleife, um alle eingegebenen Zahlen in einer Liste zu speichern
# Mit for-Schleife:  die größte und kleinste Zahl finden  -  Den Durchschnitt berechnen /Runde den Durchschnitt auf zwei Nachkommastellen.
# Die Liste sortiert (aufsteigend) ausgeben.
# Gib eine Fehlermeldung aus, wenn der Benutzer keinen gültigen Integer eingibt.




while True:

    print("\n\t\t***** Zahlen sortieren und analysieren *****\n")
    print('Geben Sie Zahlen Ihrer Wahl ein, dann Schreiben Sie "stop", um die Analyse zu starten\n')


    user_numbers = []


 #  alle eingegebenen Zahlen in der leeren Liste (user_numbers)speichern

    while True:
        user_input = input('Geben Sie eine Zahl oder "stop" ein: ')
    
        if user_input.lower() == 'stop':
            break
    
        try:
            number = float(user_input.replace(",", "."))
            user_numbers.append(number)
    
        except ValueError:
            print('Ungültige Eingabe. Bitte geben Sie eine Zahl oder "stop" ein.\n')


# Mit for-Schleife:  die größte und kleinste Zahl finden  -  Den Durchschnitt berechnen und auf zwei Nachkommastellen runden

    if user_numbers:    # Überprüfen, ob die Liste nicht leer ist

        min_number = user_numbers[0]
        max_number = user_numbers[0]
        sum_numbers = 0

        for num in user_numbers:
            if num < min_number:
                min_number = num
            if num > max_number:
                max_number = num
            sum_numbers += num

        print("\n\t\t***** Analyse-Ergebnisse *****")
        print("\n- Sortierte Liste Ihrer Zahlen:", sorted(user_numbers)) # Die Liste sortiert (aufsteigend) ausgeben
        print("\n- Größte Zahl:", max_number)
        print("\n- Kleinste Zahl:", min_number)
        print("\n- Durchschnitt (Mittelwert):", round(sum_numbers / len(user_numbers), 2), "\n") # Durchschnitt berechnen und auf zwei Nachkommastellen runden

    else:
        print("\nKeine Zahlen eingegeben. Bitte geben Sie Zahlen Ihrer Wahl ein, um die Analyse durchzuführen.\n")


# Benutzer fragen, ob er weitermachen möchte
    again = input("\n* Möchten Sie das Programm erneut ausführen? (ja/nein): ").lower()
    if again != "ja":
        print("\nProgramm beendet. Vielen Dank!")
        break