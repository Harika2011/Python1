import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        label_result.config(text=f"Product: {product}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Product Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Product", command=calculate_product)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="Product: ")
label_result.pack(pady=10)

root.mainloop()
