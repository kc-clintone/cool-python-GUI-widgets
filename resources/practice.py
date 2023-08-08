import tkinter as tk
from tkinter import ttk

#---functions---
def mouse_pos(event):
    print(f'x: {event.x}, y: {event.y}')
# window
window = tk.Tk()
window.geometry('600x500')
window.title('Learning events')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'Button')
btn.pack()

#---events---
window.bind('<Alt-KeyPress-a>', lambda event: print(event))
window.bind('<KeyPress>', lambda event: print(f'You pressed: {event.char}'))
text.bind('<Motion>', mouse_pos)

# Run the program
window.mainloop()