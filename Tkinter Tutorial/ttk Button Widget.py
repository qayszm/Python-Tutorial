
#----------------------- ttk Button Widget------------

import tkinter as tk
from tkinter import ttk

# Funktion definieren
def say_hello():
    print("Hello, danke das du mich geklickt hast!")


root = tk.Tk()
root.geometry("400x400")

# Button widget in Haupt-Fenster (root) platzieren
# command Option um Aktion zu machen Z.B. Funktion aufrufen ohne runde klammern ()

button1= ttk.Button(root, text="Klick mich!", padding=50, command=say_hello) # Funktion aufrufen ohne runde klammern ()

# Layout Manager mit pick() Methode aufrufen, um Label widget in Haupt-Fenster zu zeigen
# side = top (default value) definiert den Platz eines widget / "bottom" / "left" /  "right"
# mit fill ="x" Parameter wird das hitergrund auf ganze platz (x Achse) / fill ="y" (y Achse) / fill ="both" => füllt den ganzen Platz Vertikal und horizontal
# expand=True Vertikal Erweiterung wie möglich auf dem Fenster
# wenn expand=True auf beiden wedgets, teilen sie (gleichmäßig) das ganze Fenster Vertikal / Erweiterung
button1.pack(side="top")

# state=tk.DISABLED um Button zu stoppen  oder tk.NORMAL (default)
button2= ttk.Button(root, text="Klick mich!", state=tk.DISABLED)
button2.pack(side="top",fill="x")

# root.destroy funktion aufrufen, um Programm zu beenden / ohne runde klammern ()
quit_button= ttk.Button(root, text="Programm Beenden", command=root.destroy) 
quit_button.pack()

#----------------------------------

# Liste von alle Option keys, die mann kann mit Buttom  benutzen (padding, compound,width, image,  Style .....)
#print(button1.keys())   oder als liste
for item in button1.keys():
    print(item,": ", button1[item])




root.mainloop()