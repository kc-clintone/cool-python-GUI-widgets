import tkinter as tk
from tkinter import ttk
from random import choice

#app
app = tk.Tk()
app.geometry('600x400')
app.title('Excel')

#dummy_data
f_names = ['Gary', 'Simon', 'Greg', 'David', 'Will', 'Bill', 'Val', 'Gill', 'Bob', 'Anne', 'Jane']
s_names = ['Merryweather', 'Sympson', 'Hillcrest', 'Goldberg', 'Thompson', 'Wellwill', 'Ambers',
'Anderson', 'Winterstorm', 'Pitterson', 'Robertson']

#main
excel = ttk.Treeview(app, columns = ('f','s','e'), show = 'headings')
excel.heading('f', text = 'First Name')
excel.heading('s', text = 'Second Name')
excel.heading('e', text = 'Email Addr')
excel.pack(fill = 'both', expand = 'True')

#events
def _delete(_):
    for i in excel.selection():
        excel.delete(i)
    # excel.selection_clear
    print('Item deleted')

def selected(_):
    print(excel.selection())
    for i in excel.selection():
        print(excel.item(i)['values'])
excel.bind('<<TreeviewSelect>>', selected)
excel.bind('<Delete>', _delete)

#insert
# excel.insert(parent = '', index = 0, values = ('Kaysee', 'Jill', 'kc@gmail.com'))
for i in range(100):
    _f = choice(f_names)
    _s = choice(s_names)
    _e = f'{_f}{_s}@gmail.com'
    details = (_f, _s, _e)
    excel.insert(parent = '', index = 0, values = details)
#exec
app.mainloop()
