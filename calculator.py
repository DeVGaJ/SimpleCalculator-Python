import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_var = tk.StringVar()

        # Create display
        display = tk.Entry(root, textvariable=self.input_var, font=("Arial", 18),
                           bd=10, insertwidth=4, width=14, justify='right')
        display.grid(row=0, column=0, columnspan=4)

        # Button definitions (text, row, column)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)  # spans 4 columns
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            if text == '=':
                b = tk.Button(root, text=text, padx=20, pady=20, command=self.evaluate,
                              bg="lightblue", font=("Arial", 14))
                b.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
            elif text == 'C':
                b = tk.Button(root, text=text, padx=20, pady=20, command=self.clear,
                              bg="orange", font=("Arial", 14))
                b.grid(row=row, column=col, columnspan=colspan)
            else:
                b = tk.Button(root, text=text, padx=20, pady=20,
                              command=lambda t=text: self.append(t),
                              font=("Arial", 14))
                b.grid(row=row, column=col, columnspan=colspan)

        # Make columns expand equally
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def append(self, char):
        self.expression += str(char)
        self.input_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_var.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_var.set(result)
            self.expression = result
        except Exception:
            self.input_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()