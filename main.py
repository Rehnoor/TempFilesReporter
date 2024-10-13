import os
import script
import tkinter as tk

window = tk.Tk()
window.title("Temp File Reporter")
window.geometry("300x300")

print(script.tempFiles)


window.mainloop()
# psg.popup("Hello World")