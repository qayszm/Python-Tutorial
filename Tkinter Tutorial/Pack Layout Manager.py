
# ------------------- Layout Manager / Geometrie Manager / Layout Algorithm --------------------

# Sie beschreiben den Mechanismus, der dafür verantwörtlich ist, wie die Widgets im TKinter Hauptfenster organisiert, positiomiert und ausgerichtet werden
# Basis Layout Manager :
#   1- Pack layout Manager
#   2- Grid Layout Manager
#   3- Palce Layout Manager

#------------------------Pack layout Manager-----------------

import tkinter as tk

root = tk.Tk()

root.geometry("400x400")


# Backgrond für Label widget  mit bg Parameter => Farbe: Hexa Dezimal Werte oder Color-name 
# widget reserviert die ganze Zeile, aber das hitergrund passt genau das text
# side = top (default value) definiert den Platz eines widget / "bottom" / "left" /  "right"
# mit fill ="x" Parameter wird das hitergrund auf ganze platz (x Achse) / fill ="y" (y Achse) / fill ="both" => füllt den ganzen Platz Vertikal und horizontal
# expand=True Vertikal Erweiterung wie möglich auf dem Fenster
# wenn expand=True auf beiden wedgets, teilen sie (gleichmäßig) das ganze Fenster Vertikal / Erweiterung
label1 = tk.Label(root, text="Label 1", bg="green")
label1.pack(side="top", expand=True, fill="y")   # Vertikal Erweiterung auf dem ganzen Fenster, respektiert die andere widgets

label2 = tk.Label(root, text="Label 2", bg="red")
label2.pack(side="top", expand=True, fill="both") # hitergrund füllt den ganzen horizontalen Platz 

root.mainloop()