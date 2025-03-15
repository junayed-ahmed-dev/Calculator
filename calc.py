import tkinter as tk

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        
        # Set global dark theme for widgets
        self.root.option_add("*background", "#1A1A1A")
        self.root.option_add("*foreground", "white")
        self.root.configure(bg="#1A1A1A")  

        # Force the window to refresh after launch
        self.root.after(200, self.fix_theme)

        self.expression = ""
        
        # Display screen with better contrast
        self.display = tk.Entry(root, font=("Arial", 24), bg="#000000", fg="white", bd=10, 
                                relief=tk.FLAT, justify='right', insertbackground="white")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)
        
        # Button layout with improved color contrast
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)  # Span across 4 columns
        ]
        
        for btn in buttons:
            text, row, col = btn[0], btn[1], btn[2]
            colspan = btn[3] if len(btn) == 4 else 1
            self.create_button(text, row, col, colspan)
    
    def create_button(self, text, row, col, colspan=1):
        # Default settings for buttons
        bg_color = "#333"  # Darker number buttons
        fg_color = "white"  # White text

        # Special colors for operators and the "=" button
        if text in {"+", "-", "*", "/"}:
            bg_color = "#FF9500"  # Orange for operators
        elif text == "=":
            bg_color = "#007AFF"  # Blue for equals button
        elif text == "C":
            bg_color = "#D32F2F"  # Red for Clear button

        btn = tk.Button(self.root, text=text, font=("Arial", 18), bg=bg_color, fg=fg_color, bd=5,
                        relief=tk.RAISED, padx=20, pady=20, width=5, height=2,
                        command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, columnspan=colspan, sticky='news', padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_display()
    
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def fix_theme(self):
        """ Force UI to update correctly after launch """
        self.root.update_idletasks()
        fake_window = tk.Toplevel(self.root)
        fake_window.withdraw()  # Hidden window forces theme fix

if __name__ == "__main__":
    root = tk.Tk()
    calculator = CalculatorGUI(root)
    root.mainloop()
