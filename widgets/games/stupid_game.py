import tkinter as tk
import ttkbootstrap as ttk
import random

#======app logic=======
def change_window_position():
    # Generating random coordinates within the screen dimensions
    x = random.randint(0, app.winfo_screenwidth() - 210)
    y = random.randint(0, app.winfo_screenheight() - 210)
    app.geometry(f"210x210+{x}+{y}")

def change_text_and_buttons():
    title.config(text='I knew you were stupid.', font=("Helvetica", 12, "bold"))
    yes_btn.pack_forget()
    no_btn.pack_forget()

# =====main window=====
app = ttk.Window()
app.title("Stupid Game")
app.geometry("210x210")
app.resizable(False, False)

# -----labeled text-----
title = ttk.Label(app, text="Are you stupid?", font=("Helvetica", 12, "bold"))
title.pack(pady=20)

# ----- 'Yes' btn-----
yes_btn = tk.Button(app, text="Yes", command=change_text_and_buttons)
yes_btn.pack(side=tk.LEFT, padx=20)

# -----'No' btn------
no_btn = tk.Button(app, text="No", command=change_window_position)
no_btn.pack(side=tk.RIGHT, padx=20)

#====run app=====
app.mainloop()
