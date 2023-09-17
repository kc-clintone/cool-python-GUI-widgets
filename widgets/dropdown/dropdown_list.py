import tkinter as tk
from tkinter import ttk

# functions
# window
window = tk.Tk()
window.geometry('220x150')
window.title("A simple drop-down list")

# widget
## ---Combobox---
items = ('Tomatoes', 'Kales', 'Spinach', 'Onions', 'Garlic', 'Ginger')
groceries = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=groceries)
combo['values'] = items
combo.pack(pady=7)
combo.bind('<<ComboboxSelected>>', lambda event: print(f'You selected: {groceries.get()}'))
## ---
# run the program
window.mainloop()