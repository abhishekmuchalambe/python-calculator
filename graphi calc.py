import tkinter as tk

expression = ""  # Global variable for the calculator input

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Main program
if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="lightblue")
    gui.title("Graphical Calculator")
    gui.geometry("350x400")

    equation = tk.StringVar()

    entry_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
    entry_field.grid(row=0, column=0, columnspan=4)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            button = tk.Button(gui, text=text, fg="white", bg="green", command=equalpress, height=2, width=7)
        else:
            button = tk.Button(gui, text=text, fg="black", bg="lightgrey", command=lambda t=text: press(t), height=2, width=7)
        button.grid(row=row, column=col, padx=5, pady=5)

    clear_button = tk.Button(gui, text="C", fg="white", bg="red", command=clear, height=2, width=32)
    clear_button.grid(row=5, column=0, columnspan=4)

    gui.mainloop()
