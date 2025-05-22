import tkinter as tk
from tkinter import font as tkfont
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Base styles
        self.bg_color, self.display_color = "#2E3440", "#3B4252"
        self.btn_color, self.btn_color_alt = "#3B4252", "#4C566A"
        self.text_color, self.accent_color = "#E5E9F0", "#88C0D0"
        
        # Mode settings
        self.mode_settings = {
            "young": ("#5E81AC", "#81A1C1", "#ECEFF4", 18, 6, 2),
            "adult": ("#4C566A", "#434C5E", "#E5E9F0", 14, 6, 2),
            "system": ("#3B4252", "#4C566A", "#E5E9F0", 12, 5, 2)
        }
        
        # Scientific functions
        self.sci_map = {
            'sin': 'math.sin', 'cos': 'math.cos', 'tan': 'math.tan',
            'log': 'math.log10', 'ln': 'math.log', '√': 'math.sqrt'
        }
        
        self.root.configure(bg=self.bg_color)
        self.show_mode_selection()
    
    def clear_widgets(self):
        for widget in self.root.winfo_children(): widget.destroy()
    
    def make_header(self, text):
        tk.Label(self.root, text=text, font=tkfont.Font(family="Helvetica", size=20, weight="bold"),
                bg=self.bg_color, fg=self.accent_color).pack(pady=30)
    
    def make_button(self, text, command, is_alt=False):
        btn = tk.Button(self.root, text=text, font=tkfont.Font(family="Helvetica", size=14),
                      bg=self.btn_color_alt if is_alt else self.btn_color, fg=self.text_color,
                      command=command)
        btn.pack(pady=15, ipadx=20, ipady=10)
        return btn
    
    def show_mode_selection(self):
        self.clear_widgets()
        self.make_header("Select Calculator Mode")
        self.make_button("User-Centric", self.user_centric_mode)
        self.make_button("System-Centric", lambda: self.create_calculator("system"))
    
    def user_centric_mode(self):
        self.clear_widgets()
        self.make_header("Select Your Age Group")
        self.make_button("10-20 Years", lambda: self.create_calculator("young"))
        self.make_button("20+ Years", lambda: self.create_calculator("adult"))
        self.make_button("Back", self.show_mode_selection, True)
    
    def create_calculator(self, mode):
        self.clear_widgets()
        
        # Initialize calculator state
        self.current_input = ""
        self.total_expression = ""
        self.display_var = tk.StringVar()
        
        # Apply mode settings
        self.btn_color, self.btn_color_alt, self.text_color, font_size, btn_w, btn_h = self.mode_settings[mode]
        button_font = tkfont.Font(family="Helvetica", size=font_size)
        
        # Create display
        display_frame = tk.Frame(self.root, height=100, bg=self.display_color)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        tk.Label(display_frame, textvariable=self.display_var, anchor="e", 
                bg=self.display_color, fg=self.text_color,
                font=tkfont.Font(family="Helvetica", size=24)).pack(expand=True, fill="both", padx=20, pady=5)
        
        # Create button grid
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Define button layout
        buttons = [
            ('7', '8', '9', '/', '⌫'),
            ('4', '5', '6', 'x', 'C'),
            ('1', '2', '3', '-', '('),
            ('0', '.', '=', '+', ')')
        ]
        
        # Add scientific buttons for system mode
        if mode == "system":
            buttons = [('sin', 'cos', 'tan', '^', '√'), ('log', 'ln', 'π', 'e', 'Sci')] + buttons
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(button_frame, text=btn_text, font=button_font,
                             bg=self.btn_color, fg=self.text_color,
                             command=lambda x=btn_text: self.on_button_click(x))
                btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew", ipadx=btn_w, ipady=btn_h)
                button_frame.grid_columnconfigure(j, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)
        
        # Add back button
        tk.Button(self.root, text="Back", font=button_font, bg=self.btn_color_alt, fg=self.text_color,
                command=self.show_mode_selection).pack(pady=10, ipadx=10, ipady=5)
        
        self.update_display()
    
    def on_button_click(self, btn):
        if btn == 'C':
            self.current_input = self.total_expression = ""
        elif btn == '⌫':
            self.current_input = self.current_input[:-1]
        elif btn == '=':
            try:
                # Process expression
                expr = self.total_expression.replace('π', str(math.pi)).replace('e', str(math.e))
                
                # Replace multiplication symbol 'x' with '*'
                expr = expr.replace('x', '*')
                
                # Replace scientific functions
                for func, math_func in self.sci_map.items():
                    if func + '(' in expr:
                        expr = expr.replace(func + '(', math_func + '(')
                
                # Handle power operator
                if '^' in expr: expr = expr.replace('^', '**')
                
                # Calculate result
                result = str(eval(expr))
                self.current_input = self.total_expression = result
            except Exception:
                self.current_input = "Error"
                self.total_expression = ""
        elif btn == 'Sci':
            self.create_calculator("system")
        else:
            # Handle input of operators and functions
            if btn in self.sci_map:
                self.current_input += btn + '('
            else:
                self.current_input += str(btn)
            self.total_expression = self.current_input
        
        self.update_display()
    
    def update_display(self):
        self.display_var.set(self.total_expression)
        # Adjust font size based on content length
        size = 18 if len(self.display_var.get()) > 15 else 24
        font = tkfont.Font(family="Helvetica", size=size)
        
        # Update display label font
        for w in self.root.winfo_children():
            if isinstance(w, tk.Frame) and w.winfo_children():
                label = w.winfo_children()[0]
                if isinstance(label, tk.Label):
                    label.config(font=font)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()