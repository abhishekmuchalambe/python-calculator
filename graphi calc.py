import tkinter as tk
from tkinter import ttk

expression = ""  # Global variable for the calculator input

def press(num):
    """Handles button press"""
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    """Handles = button press"""
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    """Clears the input"""
    global expression
    expression = ""
    equation.set("")

# Main Program
if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Graphical Calculator")
    gui.geometry("360x500")
    gui.configure(bg="#1e1e2f")  # Dark theme background

    equation = tk.StringVar()

    # Style configuration
    style = ttk.Style()
    style.configure("TButton",
                    font=("Arial", 16, "bold"),
                    padding=10)

    # Entry field
    entry_field = tk.Entry(gui, textvariable=equation,
                           font=('Arial', 24, 'bold'),
                           bg="#2a2a3b", fg="white",
                           bd=10, insertwidth=2, width=15,
                           borderwidth=4, relief="ridge", justify="right")
    entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

    # Buttons (with colors)
    buttons = [
        ('7', 1, 0, "#3b3b4f"), ('8', 1, 1, "#3b3b4f"), ('9', 1, 2, "#3b3b4f"), ('/', 1, 3, "#ff9f1c"),
        ('4', 2, 0, "#3b3b4f"), ('5', 2, 1, "#3b3b4f"), ('6', 2, 2, "#3b3b4f"), ('*', 2, 3, "#ff9f1c"),
        ('1', 3, 0, "#3b3b4f"), ('2', 3, 1, "#3b3b4f"), ('3', 3, 2, "#3b3b4f"), ('-', 3, 3, "#ff9f1c"),
        ('0', 4, 0, "#3b3b4f"), ('.', 4, 1, "#3b3b4f"), ('=', 4, 2, "#2ec4b6"), ('+', 4, 3, "#ff9f1c"),
    ]

    for (text, row, col, color) in buttons:
        if text == "=":
            button = tk.Button(gui, text=text, bg=color, fg="white",
                               font=("Arial", 16, "bold"),
                               command=equalpress, height=2, width=7, relief="flat")
        else:
            button = tk.Button(gui, text=text, bg=color, fg="white",
                               font=("Arial", 16, "bold"),
                               command=lambda t=text: press(t), height=2, width=7, relief="flat")
        button.grid(row=row, column=col, padx=5, pady=5)

    # Clear button (spanning full width)
    clear_button = tk.Button(gui, text="C", bg="#e63946", fg="white",
                             font=("Arial", 16, "bold"),
                             command=clear, height=2, width=32, relief="flat")
    clear_button.grid(row=5, column=0, columnspan=4, pady=10)

    gui.mainloop()
