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
label = ttk.Label(frame, text = "Text outside frame2")
label.pack()

label2 = ttk.Label(frame2, text = "Text inside frame2")
label2.pack()

label3 = ttk.Label(app, text = "Text inside frame")
label3.pack()

app.mainloop()
