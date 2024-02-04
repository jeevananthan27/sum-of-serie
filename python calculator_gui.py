import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        if calculator_type.get() == "Basic":
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            operator = operator_var.get()

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Division by zero is not allowed.")
                    return
            else:
                messagebox.showerror("Error", "Invalid operator")
                return

            result_label.config(text=f"Result: {result}")

        elif calculator_type.get() == "Scientific":
            num = float(entry_num_sci.get())
            sci_choice = sci_choice_var.get()

            if sci_choice == "Square Root":
                result = math.sqrt(num)
            elif sci_choice == "Sine":
                result = math.sin(math.radians(num))
            elif sci_choice == "Cosine":
                result = math.cos(math.radians(num))
            elif sci_choice == "Tangent":
                result = math.tan(math.radians(num))
            else:
                messagebox.showerror("Error", "Invalid choice")
                return

            result_label.config(text=f"Result: {result}")

        elif calculator_type.get() == "BMI":
            weight = float(entry_weight.get())
            height = float(entry_height.get())

            if weight > 0 and height > 0:
                bmi = weight / (height ** 2)
                result_label.config(text=f"Your BMI is: {bmi:.2f}")
            else:
                messagebox.showerror("Error", "Invalid input. Please enter positive values for weight and height.")
                return

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_operator.delete(0, tk.END)
    entry_num_sci.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="Result:")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create variables
calculator_type = tk.StringVar()
operator_var = tk.StringVar()
sci_choice_var = tk.StringVar()

# Create widgets
label_type = tk.Label(window, text="Select Calculator Type:")
label_type.grid(row=0, column=0, columnspan=3, pady=10)

radio_basic = tk.Radiobutton(window, text="Basic", variable=calculator_type, value="Basic")
radio_basic.grid(row=1, column=0, pady=5)

radio_scientific = tk.Radiobutton(window, text="Scientific", variable=calculator_type, value="Scientific")
radio_scientific.grid(row=1, column=1, pady=5)

radio_bmi = tk.Radiobutton(window, text="BMI", variable=calculator_type, value="BMI")
radio_bmi.grid(row=1, column=2, pady=5)

# Basic Calculator widgets
label_num1 = tk.Label(window, text="Enter the first number:")
label_num1.grid(row=2, column=0, pady=5)

entry_num1 = tk.Entry(window)
entry_num1.grid(row=2, column=1, pady=5)

label_operator = tk.Label(window, text="Enter the operator (+, -, *, /):")
label_operator.grid(row=2, column=2, pady=5)

entry_operator = tk.Entry(window, textvariable=operator_var)
entry_operator.grid(row=2, column=3, pady=5)

label_num2 = tk.Label(window, text="Enter the second number:")
label_num2.grid(row=3, column=0, pady=5)

entry_num2 = tk.Entry(window)
entry_num2.grid(row=3, column=1, pady=5)

# Scientific Calculator widgets
label_num_sci = tk.Label(window, text="Enter a number:")
label_num_sci.grid(row=4, column=0, pady=5)

entry_num_sci = tk.Entry(window)
entry_num_sci.grid(row=4, column=1, pady=5)

label_sci_choice = tk.Label(window, text="Select operation:")
label_sci_choice.grid(row=4, column=2, pady=5)

sci_menu = tk.OptionMenu(window, sci_choice_var, "Square Root", "Sine", "Cosine", "Tangent")
sci_menu.grid(row=4, column=3, pady=5)

# BMI Calculator widgets
label_weight = tk.Label(window, text="Enter your weight in kilograms:")
label_weight.grid(row=5, column=0, pady=5)

entry_weight = tk.Entry(window)
entry_weight.grid(row=5, column=1, pady=5)

label_height = tk.Label(window, text="Enter your height in meters:")
label_height.grid(row=5, column=2, pady=5)

entry_height = tk.Entry(window)
entry_height.grid(row=5, column=3, pady=5)

# Buttons
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.grid(row=6, column=2, columnspan=2, pady=10)

# Result label
result_label = tk.Label(window, text="Result:")
result_label.grid(row=7, column=0, columnspan=4, pady=10)

# Start the main loop
window.mainloop()
