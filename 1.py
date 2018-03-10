
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

root = Tk()
root.title("Calc")

bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=",
"0", ".", "±",  "C",
"3,14(Пi)"
 ]
 
#логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключить написание писем
        str1 = "-+0123456789.*/"
        if textbox.get()[0] not in str1:
            textbox.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        try:
            result = eval(textbox.get())
            textbox.insert(END, "=" + str(result))
        except:
            textbox.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
       
#очистка поля 
    elif key == "C":
        textbox.delete(0, END)

    else:
        if "=" in textbox.get():
            textbox.delete(0, END)
        textbox.insert(END, key)
 

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1
textbox = Entry(root, width = 33)
textbox.grid(row=0, column=0, columnspan=5)
       
root.mainloop()
