import tkinter as tk
from tkinter import messagebox

def scan_virus():
    messagebox.showwarning("Warning", "Stop! Virus Found.")

root = tk.Tk()
root.title("Virus Scanner")
root.geometry("300x200")

scan_button = tk.Button(root, text="Scan for the virus", command=scan_virus, font=("Arial", 12))
scan_button.pack(pady=50)

root.mainloop()
