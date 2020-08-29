import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

import random

def dispLabel():
    kuji=["大吉","中吉","小吉","凶"]
    bl.configure(text=random.choice(kuji))

bl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH",command = dispLabel)

bl.pack()
btn.pack()
tk.mainloop()

