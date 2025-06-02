
import tkinter as tk

# Haupt-Fenster der GUI programm => Tk() Objekt von tkinter library (tk) benutzen => In Variable root speichern

root = tk.Tk()

# Titel für das Haupt-Fenster ändern (by default tk)

root.title("Da ist Tiltel")


# Standard Größe des Fenster mit geometry() Funktion mit Argument als String  ("BereitxHöhe") in 
# aber kann man mit Maus das Fenster danach vergrößen oder verkleinen 


root.geometry("400x400")


# mindest Geöße und max Größe ergänzen
# kann man mit Maus diese Gößen des Fensters nicht überschreiten

root.minsize(width=250, height=250)
root.maxsize(width=600, height=800)

# Feste Geöße wie Standard , kann man mit Maus das Fenster danach nicht vergrößen oder verkleinen 

#  root.resizable(width=False, height=False)
#  root.resizable(width=False, height=True)  # nur die Höhe zwischen minsize und maxsize Ändern




# Label widget (Text) in Haupt-Fenster (root) platzieren => Layout Manager mit pick() Methode aufrufen

label1 = tk.Label(root, text="Hallo Welt!")
label1.pack()



root.mainloop()