import tkinter as tk
from tkinter import ttk
from random import choice

#====app window=====
app = tk.Tk()
app.geometry('610x410')
app.title('Fake Excel')

#-----dummy_data-----
f_names = ['Gary', 'Simon', 'Greg', 'David', 'Will', 'Bill', 'Val', 'Gill', 'Bob', 'Anne', 'Jane']
s_names = ['Merryweather', 'Sympson', 'Hillcrest', 'Goldberg', 'Thompson', 'Wellwill', 'Ambers',
'Anderson', 'Winterstorm', 'Pitterson', 'Robertson']

#=====main=====
excel = ttk.Treeview(app, columns = ('f','s','e'), show = 'headings')
excel.heading('f', text = 'First Name')
excel.heading('s', text = 'Second Name')
excel.heading('e', text = 'Email Addr')
excel.pack(fill = 'both', expand = 'True')

#=====events=====
def _dlt_entry(_):
    for i in excel.selection():
        excel.delete(i)
    print('Success, item deleted')

def selected_entry(_):
    print(excel.selection())
    for i in excel.selection():
        print(excel.item(i)['values'])
excel.bind('<<TreeviewSelect>>', selected_entry)
excel.bind('<Delete>', _dlt_entry)

#-----insert an item(row)-----
for i in range(100):
    _fn = choice(f_names)
    _sn = choice(s_names)
    _em = f'{_fn}{_sn}@gmail.com'
    details = (_fn, _sn, _em)
    excel.insert(parent = '', index = 0, values = details)
#=====run application======
app.mainloop()
