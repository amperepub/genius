import math
import tkinter as tk
from tkinter import simpledialog, messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Square root of a negative number"

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def text_calculator():
    print("Scientific Calculator - Text Mode")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    while True:
        choice = input("Select an operation (0 to exit): ")

        if choice == '0':
            print("Exiting the calculator.")
            break
        
        if choice in {'1', '2', '3', '4', '5'}:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {power(num1, num2)}")

        elif choice in {'6', '7', '8', '9'}:
            num = float(input("Enter a number: "))
        
            if choice == '6':
                print(f"Result: {square_root(num)}")
            elif choice == '7':
                print(f"Result: {sine(num)}")
            elif choice == '8':
                print(f"Result: {cosine(num)}")
            elif choice == '9':
                print(f"Result: {tangent(num)}")
        else:
            print("Invalid operation. Please try again.")

def gui_calculator():
    def calculate():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            operation = operation_var.get()
            
            if operation == "Addition":
                result = add(num1, num2)
            elif operation == "Subtraction":
                result = subtract(num1, num2)
            elif operation == "Multiplication":
                result = multiply(num1, num2)
            elif operation == "Division":
                result = divide(num1, num2)
            elif operation == "Power":
                result = power(num1, num2)
            elif operation == "Square Root":
                result = square_root(num1)
                num2 = ""
            elif operation == "Sine":
                result = sine(num1)
                num2 = ""
            elif operation == "Cosine":
                result = cosine(num1)
                num2 = ""
            elif operation == "Tangent":
                result = tangent(num1)
                num2 = ""
            else:
                result = "Invalid operation"
                
            messagebox.showinfo("Result", f"Result: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    root = tk.Tk()
    root.title("Genius Calculator")

    tk.Label(root, text="First number:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()

    tk.Label(root, text="Second number:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    operation_var = tk.StringVar(value="Addition")
    operations = ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root", "Sine", "Cosine", "Tangent"]
    operation_menu = tk.OptionMenu(root, operation_var, *operations)
    operation_menu.pack()

    calc_button = tk.Button(root, text="Calculate", command=calculate)
    calc_button.pack()

    root.mainloop()

def main():
    mode = input("Do you want to use Genius Calculator in Text (T) or GUI (G) mode? ").strip().upper()
    
    if mode == 'T':
        text_calculator()
    elif mode == 'G':
        gui_calculator()
    else:
        print("Invalid option. Closing the program.")

if __name__ == "__main__":
    main()
