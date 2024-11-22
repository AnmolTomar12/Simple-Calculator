import tkinter as tk

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    
    gui = tk.Tk()

    gui.configure(background="light gray")

    gui.title("Simple Calculator")


    gui.geometry("350x400")

    expression = ""
    equation = tk.StringVar()

    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 20, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
    expression_field.grid(columnspan=4, ipadx=8, ipady=10)

    button1 = tk.Button(gui, text=' 1 ', fg='black', bg='light blue', command=lambda: press(1), height=2, width=5, font=('Arial', 14, 'bold'))
    button1.grid(row=2, column=0, padx=5, pady=5)

    button2 = tk.Button(gui, text=' 2 ', fg='black', bg='light blue', command=lambda: press(2), height=2, width=5, font=('Arial', 14, 'bold'))
    button2.grid(row=2, column=1, padx=5, pady=5)

    button3 = tk.Button(gui, text=' 3 ', fg='black', bg='light blue', command=lambda: press(3), height=2, width=5, font=('Arial', 14, 'bold'))
    button3.grid(row=2, column=2, padx=5, pady=5)

    button4 = tk.Button(gui, text=' 4 ', fg='black', bg='light blue', command=lambda: press(4), height=2, width=5, font=('Arial', 14, 'bold'))
    button4.grid(row=3, column=0, padx=5, pady=5)

    button5 = tk.Button(gui, text=' 5 ', fg='black', bg='light blue', command=lambda: press(5), height=2, width=5, font=('Arial', 14, 'bold'))
    button5.grid(row=3, column=1, padx=5, pady=5)

    button6 = tk.Button(gui, text=' 6 ', fg='black', bg='light blue', command=lambda: press(6), height=2, width=5, font=('Arial', 14, 'bold'))
    button6.grid(row=3, column=2, padx=5, pady=5)

    button7 = tk.Button(gui, text=' 7 ', fg='black', bg='light blue', command=lambda: press(7), height=2, width=5, font=('Arial', 14, 'bold'))
    button7.grid(row=4, column=0, padx=5, pady=5)

    button8 = tk.Button(gui, text=' 8 ', fg='black', bg='light blue', command=lambda: press(8), height=2, width=5, font=('Arial', 14, 'bold'))
    button8.grid(row=4, column=1, padx=5, pady=5)

    button9 = tk.Button(gui, text=' 9 ', fg='black', bg='light blue', command=lambda: press(9), height=2, width=5, font=('Arial', 14, 'bold'))
    button9.grid(row=4, column=2, padx=5, pady=5)

    button0 = tk.Button(gui, text=' 0 ', fg='black', bg='light blue', command=lambda: press(0), height=2, width=5, font=('Arial', 14, 'bold'))
    button0.grid(row=5, column=0, padx=5, pady=5)

    plus = tk.Button(gui, text=' + ', fg='black', bg='light green', command=lambda: press("+"), height=2, width=5, font=('Arial', 14, 'bold'))
    plus.grid(row=2, column=3, padx=5, pady=5)

    minus = tk.Button(gui, text=' - ', fg='black', bg='light green', command=lambda: press("-"), height=2, width=5, font=('Arial', 14, 'bold'))
    minus.grid(row=3, column=3, padx=5, pady=5)

    multiply = tk.Button(gui, text=' * ', fg='black', bg='light green', command=lambda: press("*"), height=2, width=5, font=('Arial', 14, 'bold'))
    multiply.grid(row=4, column=3, padx=5, pady=5)

    divide = tk.Button(gui, text=' / ', fg='black', bg='light green', command=lambda: press("/"), height=2, width=5, font=('Arial', 14, 'bold'))
    divide.grid(row=5, column=3, padx=5, pady=5)

    equal = tk.Button(gui, text=' = ', fg='black', bg='orange', command=equalpress, height=2, width=5, font=('Arial', 14, 'bold'))
    equal.grid(row=5, column=2, padx=5, pady=5)

    clear = tk.Button(gui, text='Clear', fg='black', bg='red', command=clear, height=2, width=5, font=('Arial', 14, 'bold'))
    clear.grid(row=5, column=1, padx=5, pady=5)

    decimal = tk.Button(gui, text='.', fg='black', bg='light blue', command=lambda: press('.'), height=2, width=5, font=('Arial', 14, 'bold'))
    decimal.grid(row=6, column=0, padx=5, pady=5)

    gui.mainloop()