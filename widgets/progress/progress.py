import tkinter as tk
from tkinter import ttk
#====main window=====
app = tk.Tk()
app.title("Progress bars")
app.geometry('200x600')

vertical = tk.DoubleVar(value = 15)
scl = ttk.Scale(
    app,
    command = lambda value: print(vertical.get()),
    from_ = 0,
    to = 30,
    length = 300,
    orient = 'vertical',
    variable = vertical
)
scl.pack()

progress = ttk.Progressbar(
    app,
    variable = vertical,
    maximum = 30,
    orient = 'horizontal',
    length = 400
)
progress.pack()

app.mainloop()
