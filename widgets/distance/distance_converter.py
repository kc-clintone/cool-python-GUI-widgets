import tkinter as tk
import ttkbootstrap as ttk
#====app logic====
def convert_logic():
	miles = user_entry.get()
	result = miles * 1.61
	output_placeholder.set(result)

#-----application window-------
app = ttk.Window(themename = 'darkly')
app.title("Dist-Convert")
app.geometry('350x160')

#------App title-------
title_label = ttk.Label(master = app, text = 'Miles To Kilometers', font = 'Calibri 18 bold')
title_label.pack()

#-----input field-------
container = ttk.Frame(master = app)
user_entry = tk.IntVar()
input_field = ttk.Entry(master = container, textvariable = user_entry)
button = ttk.Button(master = container, text = 'Convert', command = convert_logic)
input_field.pack(side = 'left', padx = 10)
button.pack(side = 'left')
container.pack(pady = 10)

#------output field------
output_placeholder = tk.StringVar()
output_label = ttk.Label(master = app, text = 'output', font = 'Calibri 15', textvariable = output_placeholder)
output_label.pack(pady = 4)

#------run/debug------
app.mainloop()
