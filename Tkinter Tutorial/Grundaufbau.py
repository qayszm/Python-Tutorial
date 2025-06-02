
import tkinter as tk

# Test Funktion von tkinter library
#       tk._test()

#-------------------------------------

# Haupt-Fenster der GUI programm
# Tk() Objekt von tkinter library (tk) benutzen => In Variable root speichern

root = tk.Tk()

# Label widget (Text) in Haupt-Fenster (root) platzieren

label1 = tk.Label(root, text="Hallo Welt!")


# Layout Manager mit pick() Methode aufrufen, um Label widget in Haupt-Fenster zu zeigen

label1.pack()



root.mainloop()

# Evenrt loop / mainloop aufrufen, um das Programm durchzuführen
# Evenrt loop:  Endlosschleife, die permanent prüft, ob ein Event auftritt
# mainloop: ist die letzte Zeile des Programms
# mainloop macht Breake => Stoppt alle Befehle danach, Bis zu das Haupt-Fenster schließen

print("Diese Code wird nach Schließen des Programms durchgeführt werden")
