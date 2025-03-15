#Write a Python program to create an application that accepts a password from the user and displays its strength based on the length of the password using the Python Tkinter library.

import tkinter as tk

def check_password_strength():
    password = password_entry.get()
    password_length = len(password)
    
    if password_length < 6:
        strength_label.config(text="Password strength: Weak", fg="red")
    elif 6 <= password_length < 10:
        strength_label.config(text="Password strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password strength: Strong", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=20)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="Password strength: Not checked", fg="black")
strength_label.pack(pady=5)

root.mainloop()
