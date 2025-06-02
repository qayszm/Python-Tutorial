
#-------------------- ttk widget  (Themed Tkinter)------------------------

# more modern and native to the OS
#  is a separate part of Tkinter: from tkinter import ttk.
#  Supports themes (via ttk.Style())
#  Advanced widgets like Treeview, Notebook, Progressbar, etc.

# Pillow-Paket installieren
# in Terminal :  
# pip install pillow

# Pillow-Paket upgrade:
# python.exe -m pip install --upgrade pip

#Installation prüfen
#python -c "import PIL; print(PIL.__version__)"


import tkinter as tk
from tkinter import ttk

# Import Image from Pillow Paket
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("400x400")

#--------------------------------------
# TTK Label widget (Text) in Haupt-Fenster (root) platzieren => Layout Manager mit pick() Methode aufrufen
#label1 = ttk.Label(root, text="TTk Label1")
#label1.pack()

# TTK Label widget (Text) in Configure Methode => alle Optionen können in Configure Methode geschriben werden
#label2 = ttk.Label(root)
#label2.pack()

#label2.configure(text="TTk Labe2")

#------------------------------------------

# Zugriff auf einen Bild: mit Image.open(Pfad) Methode => Öffnen  einrn Bild in image vriable

image = Image.open("img1.jpg")

# Bild in Label integrieren mit PhotoImage(bild-Variable)

photo = ImageTk.PhotoImage(image)

label3 = ttk.Label(root, image=photo)
label3.pack()




root.mainloop()