
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
root.geometry("600x400")

# Style/ Theme defenieren
style = ttk.Style()
style.theme_use("clam")




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
# die Größe der Bild mit resize((Bereit, Höhe),Resampling-Filter) in pixel 
# Z.B resize((200, 200), Image.Resampling.LANCZOS)

image1 = Image.open("c:/Python-Tutorial/Tkinter Tutorial/img1.jpg").resize((200, 100))

# Bild in Label integrieren mit PhotoImage(bild-Variable)

photo1 = ImageTk.PhotoImage(image1)

#image2 = Image.open("c:/Python-Tutorial/Tkinter Tutorial/img2.jpg").resize((300, 100))
#photo2 = ImageTk.PhotoImage(image2)

# Bild und Text in einem Label
label3 = ttk.Label(root, text="Das ist ein Bild", image=photo1, compound="right") # Bild platz "top" / "left" / "bottom" / "center"
label3.pack()
label3.configure(background="red", font=("Arial", 30))   # Schrift-Art für Text und Schrift-Größe  
#Backgrond funkioniert nicht ohne Style zu definieren





# von dem zweite Bild einen Banner machen
#label3["image"] = photo2

#---------------------------
# Liste von alle Option keys, die mann kann mit Label (direct in label oder in Configure) benutzen (padding, font, Backgrround, Style .....)
#print(labe3.keys())   oder als liste
for item in label3.keys():
    print(item,": ", label3[item])



root.mainloop()