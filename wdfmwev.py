import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title
# label=tk.Label(window, text="SMS COMMAND")
# label.pack()
entry1string = tk.StringVar()


def retrieveData():
  #retrieve it into a variable
  print(entry1string.get())
  #print the data

  #Or output the data on the window in a Label :


# create an entry box
entry = ttk.Entry(window, width=20)
entry.grid(row=0, column=0, padx=5, pady=5)
#create a button
btn = ttk.Button(window, text='Submit', command=retrieveData)
btn.grid(row=1, column=0)

# create a list box
listbox = tk.Listbox(window, width=20, height=5)
listbox.grid(row=0, column=4, padx=5, pady=5)

# add items to the list box
for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
  listbox.insert(tk.END, item)

# create a combo box
combo = ttk.Combobox(window,
                     values=["GPRSSTATUS", "VERSION", "SYSSTATUS", "WEBSTART"])
combo.grid(row=0, column=8, padx=5, pady=5)
#button for list
btn = ttk.Button(window, text='Submit')
btn.grid(row=1, column=8)

window.mainloop()
