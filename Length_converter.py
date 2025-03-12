#Write a Python program to create an application length 
# in inches as input from the user and return the value of that length in centimeters 
# using the Python Tkinter library.


import tkinter as tk

def convert_to_cm():
    inches = float(entry.get())
    centimeters = inches * 2.54
    result_label.config(text=f"{inches} inches is equal to {centimeters} cm")

root = tk.Tk()
root.title("Inches to Centimeters Converter")

input_label = tk.Label(root, text="Enter length in inches:")
input_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Result will be displayed here")
result_label.pack(pady=10)

root.mainloop()
