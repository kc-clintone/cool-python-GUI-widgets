import tkinter as tk
import ttkbootstrap as ttk

#====app logic=====
def accept():
	print('I knew it!')

def mouse_over_event(param):
	pass


app = ttk.Window()
app.title('Stupid Game')
app.geometry('150x100')

title = ttk.Label(master = app, text = 'Are you stupid?', font = 'Calibri 15')
title.pack()

container = ttk.Frame(master = app)
btn_yes = ttk.Button(master = container, text = 'Yes', command = accept)
btn_no = ttk.Button(master = container, text = 'No')

btn_yes.pack(side = 'left')
btn_no.pack(side = 'left', padx = 10)
container.pack(pady = 15)

btn_no.bind('<Motion>', lambda event: mouse_over_event(event))

app.mainloop()
