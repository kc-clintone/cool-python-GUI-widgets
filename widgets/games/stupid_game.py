import tkinter as tk
import ttkbootstrap as ttk
import random

def change_window_position():
    # Generating random coordinates within the screen dimensions
    x = random.randint(0, app.winfo_screenwidth() - 200)
    y = random.randint(0, app.winfo_screenheight() - 200)
    app.geometry(f"200x200+{x}+{y}")

def change_text_and_buttons():
    title.config(text='I knew you were stupid.', font=("Helvetica", 12, "bold"))
	container.pack_forget()
	
    # yes_btn.pack_forget()
    # no_btn.pack_forget()

# Create the main window
app = ttk.Window()
app.title("Stupid Game")
app.geometry("200x200")
app.resizable(False, False)

container = ttk.Frame(master = app)
# Create the 'Yes' button
yes_btn = tk.Button(container, text="Yes", command=change_text_and_buttons)
yes_btn.pack(side=tk.LEFT, padx=10)

# Create the 'No' button
no_btn = tk.Button(container, text="No", command=change_window_position)
no_btn.pack(side=tk.RIGHT, padx=10)
container.pack(pady = 15)


# Create the label with the text
title = ttk.Label(app, text="Are you stupid?", font=("Helvetica", 12, "bold"))
title.pack(pady=20)

app.mainloop()
