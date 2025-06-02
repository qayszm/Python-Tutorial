
#-------------------- ttk widget  (Themed Tkinter)------------------------
# ---------Tkinter Variablen (StringVar, IntVar, DoubleVar, BooleanVar)---------

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("400x400")

text_variable1 = "Text von einer Variable"

label1 = ttk.Label(root, text=text_variable1)
label1.pack()

text_variable1 = "neuer Text von einer Variable" # keine Wirkung => der Text bleibt

# Text in Label1 ändern / überschreiben
#label1.configure(text="Neue Text")           # oder        label1["text"] = "Neue Text"


#--------------------------------------------

# textVaraible / StringVar => kann man immer mit set() Methode ändern

text_variable2 = tk.StringVar()
text_variable2.set("Das ist  TextVariable")

label2 = ttk.Label(root, textvariable=text_variable2)
label2.pack()

text_variable2.set("Aktualisierte TextVariable") #  der Text wird geändert werden

#--------------------------------------------

# IntVar für ganze Zahlen => kann man immer mit set() Methode ändern

text_variable3 = tk.IntVar()
text_variable3.set(10)

label3 = ttk.Label(root, textvariable=text_variable3)
label3.pack()

text_variable3.set(20) #  der Integer wird geändert werden

#--------------------------------------------

# DoubleVar für Komma Zahlen (.) => kann man immer mit set() Methode ändern

text_variable4 = tk.DoubleVar()
text_variable4.set(10.2)

label4 = ttk.Label(root, textvariable=text_variable4)
label4.pack()

text_variable4.set(20.7) #  die Komma-Zahl wird geändert werden

#--------------------------------------------

# BooleanVar (True , False) => kann man immer mit set() Methode ändern
# es wird 0 => False oder 1 => True auf dem Fenster gezeigt

text_variable5 = tk.BooleanVar()
text_variable5.set(True)

label5 = ttk.Label(root, textvariable=text_variable5)
label5.pack()

text_variable5.set(False) #  die Komma-Zahl wird geändert werden



root.mainloop()