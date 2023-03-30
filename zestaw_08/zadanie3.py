import tkinter as tk
from tkcalendar import Calendar  # pip install tkcalendar
from datetime import datetime

okno = tk.Tk()
okno.title("Zegar i kalendarz")
okno.geometry("600x400")
okno.resizable(False, False)

string_var = tk.StringVar(okno)

def update_date_time():
    str = datetime.today().strftime('%d %b %Y\n%A %H:%M:%S')
    string_var.set(str)
    date_time.after(1000, update_date_time)

date_time = tk.Label(okno, textvariable=string_var, font=('times', 48, 'bold'))
date_time.pack(anchor="center", pady=50, padx=50)

current_time = datetime.now()

cal = Calendar(okno, year=current_time.year, month=current_time.month, day=current_time.day)
cal.pack()

update_date_time()

okno.mainloop()
