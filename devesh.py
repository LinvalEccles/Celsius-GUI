import tkinter

from tkinter import ttk

from tkinter import messagebox

def calculate():
    c = float(number.get()) 
    f = ((c*9)/(5))+32
    messagebox.showinfo(message = f)
















root =tkinter.Tk()
root.title("Celsius Calculator")
root.geometry("1600x900")
root.configure(bg="#333333")

label=tkinter.Label(root, text="Celcius Calculator",bg="#F9999F",font=("Arial,30"))
label.pack(pady=20)
number = tkinter.Entry(root,font=("Arial,18"))
number.pack(pady=20)
result = tkinter.StringVar()
btn = tkinter.Button(root, text="Calculate",command=calculate)
btn.pack(pady=20)

root.mainloop()