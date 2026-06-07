import tkinter as tk

window = tk.Tk()
window.title("My First App")

label = tk.Label(window, text="Hello, World!")
label.pack()

window.mainloop()