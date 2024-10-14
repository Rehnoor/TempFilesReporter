import os
import script
import testinit
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title("Temp File Reporter")
window.geometry("1000x1000")

columns = ("Path", "File/Folder Name", "Size", "Last Modified")

tree = ttk.Treeview(window, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)

# Grid configuration
window.columnconfigure(0, weight=1)  # Makes sure the window scales properly

# Description label
descLab = tk.Label(window, text="Please enter below which directory you would like to be scanned for temporary files:")
descLab.grid(row=0, column=0, padx=10, pady=10)

# Directory label
dirLab = tk.Label(window, text="Directory:")
dirLab.grid(row=1, column=0, padx=10, pady=10, sticky='w')

# Directory entry
dirEntry = tk.Entry(window)
dirEntry.grid(row=2, column=0, padx=10, pady=10, sticky='ew')


def stringifyBytes(bytes):
    kb = bytes/1000
    if (kb < 1):
        return str(bytes) + " Bytes"
    mb = kb/1000
    if (mb < 1):
        return str(kb) + " KB"
    gb = mb/1000
    if (gb < 1):
        return str(mb) + " MB"
    tb = gb/1000
    if (tb < 1):
        return str(gb) + " GB"
    return str(tb) + " TB"

def getInsights():
    totBytes = 0
    for tup in script.tempFiles:
        totBytes += tup[2]
    totBytes = stringifyBytes(totBytes)
    txt = "You can save " + totBytes + " of storage if you remove these files!"
    insights = tk.Label(window, text=txt)
    insights.grid(row=6, column=0, padx=10, pady=10)

def listData():
    for tup in script.tempFiles:
        tempTup = (tup[0], tup[1], stringifyBytes(tup[2]), tup[3])
        tree.insert("", tk.END, values=tempTup)

# function for processing submission
def dir_submit():
    enteredDir = dirEntry.get()
    if not os.path.exists(enteredDir):
        messagebox.showerror("Invalid directory", "You entered an invalid directory! Please enter a valid one")
    else:
        script.getTemp(enteredDir)
        printLog()
        getInsights()
        listData()





dirSub = tk.Button(window, text="Submit", command=dir_submit)
dirSub.grid(row=3, column=0, padx=10, pady=10)


tree.grid(row=5, column=0, padx=10, pady=10, sticky='ew')



def printLog():
    print("HERE ARE THE TEMPORARY FILES")
    print("----------------------------------------------------")

    for tup in script.tempFiles:
        dirpath, fName, fileSize, modTime = tup
        print("There is a temporary file called " + fName + " at the directory " + dirpath + ".")
        print("-Size: " + str(fileSize) + ", Last Modified: " + str(modTime))
        print()

    print("HERE ARE THE TEMPORARY FOLDERS")
    print("-------------------------------------------------------")
    for tup in script.tempFolders:
        dirpath, dName, fileSize, modTime = tup
        print("There is a temporary folder called " + dName + " at the directory " + dirpath)
        print("-Size: " + str(fileSize) + ", Last Modified: " + str(modTime))
        print()


window.mainloop()