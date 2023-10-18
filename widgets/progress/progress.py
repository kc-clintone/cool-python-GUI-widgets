import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#====main window=====
app = tk.Tk()
app.title("Progress bars")
app.geometry('400x500')

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

# ====progress bar=====
progress = ttk.Progressbar(
    app,
    variable = vertical,
    maximum = 30,
    orient = 'horizontal',
    length = 400
)
progress.pack()

# ====scrolled text ======
sc = scrolledtext.ScrolledText(app, height = 10)
sc.pack()
# =======numeric progress========
np = tk.IntVar()
npp = ttk.Progressbar(app, orient = 'vertical', variable = np)
npp.pack()
npp.start()

indicatr = ttk.Label(app, textvariable = np)
indicatr.pack()

app.mainloop()
