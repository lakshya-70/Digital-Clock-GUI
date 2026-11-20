# 58th github project --> Digital Clock GUI
print('----------Digital Clock GUI----------')
import tkinter as tk
from datetime import datetime


def update_clock():
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %B %d, %Y"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")

time_label = tk.Label(root, font=("Consolas", 48, "bold"),
                      fg="lime", bg="black")
time_label.pack(padx=20, pady=(20, 0))

date_label = tk.Label(root, font=("Arial", 14),
                      fg="white", bg="black")
date_label.pack(padx=20, pady=(0, 20))

update_clock()

root.mainloop()