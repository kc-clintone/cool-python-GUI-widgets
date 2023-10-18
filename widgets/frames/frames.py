import tkinter as tk
from tkinter import ttk

# ===== app ====
app = tk.Tk()
app.geometry('600x400')
app.title('Frames')

# ===== frame =====
frame = ttk.Frame(
	app,
	width = 200,
	height = 200,
	borderwidth = 10,
	relief = tk.GROOVE
)
frame.pack()

frame2 = ttk.Frame(
	frame,
	width = 90,
	height = 160,
        borderwidth = 10,
        relief = tk.GROOVE
)
frame2.pack()



# ===== frame content =====
label = ttk.Label(frame, text = "Text example")
label.pack()

label2 = ttk.Label(frame2, text = "Text outside frame")
label2.pack()

app.mainloop()
