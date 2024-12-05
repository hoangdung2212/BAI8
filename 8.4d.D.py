print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
from tkinter import *

def on_key_press(event):
    lbl.configure(text=f"Key pressed: {event.keysym}")

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)

window.bind('<KeyPress>', on_key_press)

window.mainloop()

