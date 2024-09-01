import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Retrieve input values
        a = float(entry1.get())
        b = float(entry2.get())
        operator = operator_var.get()

        # Perform the calculation
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = a / b
        else:
            messagebox.showerror("Error", "Invalid operator")
            return

        # Display the result
        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x330")  # Set window size
root.resizable(False,False)

# Create input fields and labels
tk.Label(root, text="Enter first number:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry1 = tk.Entry(root, font=('Arial', 12))
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry2 = tk.Entry(root, font=('Arial', 12))
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Operator (+, -, *, /):", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
operator_var = tk.StringVar()
operator_entry = tk.Entry(root, textvariable=operator_var, font=('Arial', 12))
operator_entry.grid(row=2, column=1, padx=10, pady=10)

# Create a button to perform the calculation
calc_button = tk.Button(root, text="Calculate", command=calculate, font=('Arial', 12), width=15)
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=('Arial', 12))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
