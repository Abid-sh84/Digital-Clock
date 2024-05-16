import tkinter as tk
from datetime import datetime

def update_clock():
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%Y-%m-%d"))
    window.after(1000, update_clock)  


window = tk.Tk()
window.title("Digital Clock")


time_label = tk.Label(window, font=("Helvetica", 48), bg="black", fg="white")
time_label.pack(pady=20)

date_label = tk.Label(window, font=("Helvetica", 24))
date_label.pack()


update_clock()

window.mainloop()
