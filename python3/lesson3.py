#TKINTER IN PYTHON . ACTIVITY-1

from tkinter import *

window =Tk()
window.title("Tkinter sample window")
window.geometry("250x100")

greeting =Label(text="hello user", fg="gray",bg="black")
button=Button(text="clickhere",bg="blue",fg="yellow")
entry=Entry(text="entry your name",bg="white",fg="black")

greeting.pack()
button.pack()
entry.pack()

textbox=Text(fg="orange",bg="green")
textbox.pack()

window.mainloop()


import ipywidgets as widgets
from IPython.display import display

grid=[]
for i in range(4):
    row=[]
    for j in range(4):
        btn=widhets.Butten(description=f'{i},{j}',Layout=widgets.Layout(width="90px"))
        row.append(btn)
    grid.append(widgets.HBox(row))
display(widgets.VBox(grid))


import tkinter as tk

window = tk.Tk()

for i in range(4):

for j in range(4):

frame= tk.Frame(

master=window,

relief=tk.RAISED,

borderwidth=1

)

frame.grid(row=i, column=j, padx=5, pady=5)

label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

label.pack()

window.mainloop()