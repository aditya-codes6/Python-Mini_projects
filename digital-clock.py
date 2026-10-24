import tkinter as tk 
from time import strftime

root = tk.Tk() #object creation
root.title("Digital Clock")  #title :- Display on screen

def time():
    String = strftime("%H:%M: %S %p \n %d-%m-%y")
    label.config(text=String)
    label.after(1000,time)

label = tk.Label(root,font =('calibri',50,'bold' ) ,background='yellow',foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
