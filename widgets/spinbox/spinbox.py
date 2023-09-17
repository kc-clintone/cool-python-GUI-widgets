import tkinter as tk
from tkinter import ttk

# functions
# window
app = tk.Tk()
app.title('A simple spinbox')
app.geometry('200x100')

# widget
#---Spinbox---
start_val = tk.IntVar(value=10)
spin = ttk.Spinbox(app, from_ = 10, to = 50, textvariable=start_val)
spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))
spin.pack(pady = 7)
# run program
app.mainloop()