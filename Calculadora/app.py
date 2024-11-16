import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display for the result
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=self.calculate)
            elif text == 'C':
                button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=self.clear)
            else:
                button = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        current_text = self.result_var.get()
        self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Erro")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
