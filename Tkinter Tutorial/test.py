
import tkinter as tk
import pygame

# Pygame für Sound vorbereiten
pygame.mixer.init()

# Zuordnung: Zahl → Sounddatei
sounds = {
    1: "sound1.mp3",
    2: "sound2.mp3",
    3: "sound3.mp3",
    4: "sound4.mp3",
    5: "sound5.mp3",
    6: "sound6.mp3"
}

def play_sound(note):
    datei = sounds.get(note)
    if datei:
        try:
            pygame.mixer.music.load(datei)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Fehler beim Abspielen: {e}")
    else:
        print("Ungültige Eingabe!")


tk.Label(root, text="Wähle eine Zahl von 1 bis 6:", font=("Arial", 12)).pack(pady=10)

for i in range(1, 7):
    tk.Button(root, text=f"{i}", width=10, height=2, command=lambda i=i: spiele_sound(i)).pack(pady=5)

root.mainloop()