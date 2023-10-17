import tkinter as tk

# function
# main app
app = tk.Tk()
app.geometry('630x430')
app.title('Simple Canvas')

#---widget
canvas = tk.Canvas(app, bg='white')
canvas.pack(pady=10)

# canvas.create_rectangle((20,20,100,200), fill = 'grey')
# canvas.create_oval(230,0,300,100)
# canvas.create_polygon((250,20, 340,45, 300,150))

# -----draw something on the canvas-----
def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill='black')

# -----increase/decrease brush size when mousewheel is used-----
def increase_brush_size(event):
    global brush_size
    if event.delta > 0:
        brush_size += 3.5
    else:
        brush_size -= 3.5
    brush_size = max(0, min(brush_size, 50))

brush_size = 2

# ---canvas window events---
canvas.bind('<Motion>', draw)
canvas.bind('MouseWheel', increase_brush_size)
# run the app
app.mainloop()
