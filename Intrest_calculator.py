#Write a Python program to create an application to take inputs of 
# the principal amount, time period, and rate of interest from the user, and return the simple interest and compound interest 
# on the same principle using the Python Tkinter library.



import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * ((1 + (rate / 100)) ** time) - principal

        result_text = (
            f"Simple Interest: ₹{simple_interest:.2f}\n"
            f"Compound Interest: ₹{compound_interest:.2f}"
        )
        result_label.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")

heading_label = tk.Label(root, text="Interest Calculator", font=("Helvetica", 18, "bold"))
heading_label.pack(pady=10)

tk.Label(root, text="Principal Amount (₹(rupees)):").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Rate of Interest (%):").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Time Period (years):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_interest, bg="green", fg="white")
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
result_label.pack()

root.mainloop()
