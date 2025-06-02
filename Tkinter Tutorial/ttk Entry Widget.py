
# ----------------- ttk Entry Widget-------------

import tkinter as tk
from tkinter import ttk

# Funktion definieren, um Entry-Eingabe mit get() Methode auszugeben
def print_entry_input():
    print(entry1.get())

# Funktion definieren, um Entry-Eingabe mit get() Methode in einem Label auf dem Haupt-Fenster auszugeben
def entry_input_in_label():
    ttk.Label(root, text=entry1.get()).pack()

# Funktion definieren, um Entry-Eingabe mit delete() Methode zu löschen
def delete_input():
    entry1.delete(0, tk.END)   # löscht ganze String (von index = 0 bis Ende)/ (0, 5) löscht erste 5 Character (nicht inklusive den letzeten)

root = tk.Tk()
root.geometry("400x400")



# Entry widget in Haupt-Fenster (root) platzieren
# width=40 in Pixel die Bereit von Entry widget
# forground Optionen um die Textfarbe zu ändern
# Backgrond funkioniert nicht ohne Style zu definieren
# justify="left" Text schreiben-Richtun links nach richts (default) / "right" / "center"
entry1 = ttk.Entry(root, width=40, foreground="red", justify="center")
# Layout Manager mit pick() Methode aufrufen, um Label widget in Haupt-Fenster zu zeigen
entry1.pack()

# insert(index, "Text")  Methode, um einen Festen (default) Text in Entry einzugeben / kann man löschen / weiterschreiben 
# index nummer definiert den Plat für den Text in der String-Kette

entry1.insert(0, "Ich möchte")
entry1.insert(3, "TEST")   # Wort TEST in der String-Kette (Index 3) hinzufügen

# command Option um Aktion zu machen Z.B. Funktion aufrufen ohne runde klammern ()
button1= ttk.Button(root, text="Entry-Eingabe in Konsole ausgeben", command=print_entry_input)
button1.pack()

button2= ttk.Button(root, text="Entry-Eingabe in Label ausgeben", command=entry_input_in_label)
button2.pack()

button3= ttk.Button(root, text="Eingabe Löschen", command=delete_input)
button3.pack()


#-----------------------------------

# Liste von alle Option keys, die mann kann mit Entry  benutzen (Font, state,width, Background,  Style .....)
#print(entry1.keys())   oder als liste
for item in entry1.keys():
    print(item,": ", entry1[item])



root.mainloop()