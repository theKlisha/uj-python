import tkinter as tk
from tkinter import END, Button, Entry
import tkinter.font as font
import operator

okno = tk.Tk()
okno.title("Calculator")

myFont = font.Font(family='Arial', size=20, weight='bold')

ans_entry = Entry(okno, bd=5, width=20, font=myFont, bg="gray", fg="white")
ans_entry.grid(row=0, column=0, columnspan=4)

buttons = {
    (0, 0): "1",
    (1, 0): "2",
    (2, 0): "3",
    (3, 0): "/",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (3, 1): "*",
    (0, 2): "7",
    (1, 2): "8",
    (2, 2): "9",
    (3, 2): "-",
    (0, 3): "C",
    (1, 3): "0",
    (2, 3): "=",
    (3, 3): "+",
}

for (x, y), v in buttons.items():
    btn = Button(okno, text=v, padx=20, pady=10)
    btn['font'] = myFont
    btn.grid(row=x+1, column=y)

op = None
prev = None

def mouse_button_release(event):
    global op
    global prev
    widg = event.widget
    text = widg.cget("text")

    if text in "0123456789":
        ans_entry.insert(len(ans_entry.get()), text)

    if text in "+-*/" and op == None:
        if text == "+": op = operator.add
        if text == "-": op = operator.sub
        if text == "*": op = operator.mul
        if text == "/": op = operator.truediv
        prev = ans_entry.get()
        ans_entry.delete(0, END)
        
    if text == "C":
        ans_entry.delete(0, END)
        prev = None
        op = None

    if text == "=" and op != None and prev != None:
        result = op(float(prev), float(ans_entry.get()))
        ans_entry.delete(0, END)
        ans_entry.insert(0, result)
        prev = None
        op = None

okno.bind("<ButtonRelease>", mouse_button_release)
okno.mainloop()
