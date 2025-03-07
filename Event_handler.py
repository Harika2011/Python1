import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

def on_key_press(event):
    label.config(text=f"Key Pressed: {event.keysym}")

root = tk.Tk()
root.title("Keypress and Button Click Events")
root.geometry("300x200")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

label = tk.Label(root, text="Press any key...", font=("Arial", 12))
label.pack()

root.bind("<KeyPress>", on_key_press)

root.mainloop()
