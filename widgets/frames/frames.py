import tkinter as tk
from tkinter import ttk

# ===== app ====
app = tk.Tk()
app.geometry('600x400')
app.title('Frames')

# ===== frame =====
frame = ttk.Frame(
	app,
	width = 100,
	height = 200,
	borderwidth = 10,
	relief = tk.GROOVE
)
frame.pack()

# ===== frame content =====
label = ttk.Label(frame, text = "Text example")
label.pack()

lebel2 = ttk.Label(app, text = "Text outside frame")
label2.pack()

app.mainloop()
