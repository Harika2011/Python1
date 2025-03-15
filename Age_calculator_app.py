import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())
        
        current_date = datetime.today()
        birth_date = datetime(birth_year, birth_month, birth_day)
        
        age = current_date.year - birth_date.year
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        result_label.config(text=f"Your age is: {age} years")
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid day, month, and year.")

root = tk.Tk()
root.title("Age Calculator")

day_label = tk.Label(root, text="Day (DD):")
day_label.pack()
day_entry = tk.Entry(root)
day_entry.pack()

month_label = tk.Label(root, text="Month (MM):")
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

year_label = tk.Label(root, text="Year (YYYY):")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack()

result_label = tk.Label(root, text="Your age will appear here.")
result_label.pack()

root.mainloop()
