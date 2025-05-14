import tkinter as tk
from tkinter import font as tkfont
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Configure styles
        self.bg_color = "#2E3440"
        self.btn_color = "#3B4252"
        self.btn_color_alt = "#4C566A"
        self.text_color = "#E5E9F0"
        self.accent_color = "#88C0D0"
        self.display_color = "#3B4252"
        
        self.root.configure(bg=self.bg_color)
        
        # Create mode selection screen
        self.create_mode_selection()
    
    def create_mode_selection(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create title
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        title = tk.Label(self.root, text="Select Calculator Mode", font=title_font, 
                         bg=self.bg_color, fg=self.accent_color)
        title.pack(pady=30)
        
        # Create mode buttons
        btn_font = tkfont.Font(family="Helvetica", size=14)
        
        user_centric_btn = tk.Button(self.root, text="User-Centric", font=btn_font,
                                    bg=self.btn_color, fg=self.text_color,
                                    command=self.user_centric_mode)
        user_centric_btn.pack(pady=15, ipadx=20, ipady=10)
        
        system_centric_btn = tk.Button(self.root, text="System-Centric", font=btn_font,
                                      bg=self.btn_color, fg=self.text_color,
                                      command=self.system_centric_mode)
        system_centric_btn.pack(pady=15, ipadx=20, ipady=10)
    
    def user_centric_mode(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create age selection screen
        title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        title = tk.Label(self.root, text="Select Your Age Group", font=title_font, 
                         bg=self.bg_color, fg=self.accent_color)
        title.pack(pady=30)
        
        btn_font = tkfont.Font(family="Helvetica", size=14)
        
        young_btn = tk.Button(self.root, text="10-20 Years", font=btn_font,
                             bg=self.btn_color, fg=self.text_color,
                             command=lambda: self.create_calculator("young"))
        young_btn.pack(pady=15, ipadx=20, ipady=10)
        
        adult_btn = tk.Button(self.root, text="20+ Years", font=btn_font,
                            bg=self.btn_color, fg=self.text_color,
                            command=lambda: self.create_calculator("adult"))
        adult_btn.pack(pady=15, ipadx=20, ipady=10)
        
        back_btn = tk.Button(self.root, text="Back", font=btn_font,
                           bg=self.btn_color_alt, fg=self.text_color,
                           command=self.create_mode_selection)
        back_btn.pack(pady=15, ipadx=20, ipady=10)
    
    def system_centric_mode(self):
        self.create_calculator("system")
    
    def create_calculator(self, mode):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Initialize calculator variables
        self.current_input = ""
        self.total_expression = ""
        self.display_var = tk.StringVar()
        self.scientific_mode = False
        
        # Adjust UI based on mode
        if mode == "young":
            self.btn_color = "#5E81AC"
            self.btn_color_alt = "#81A1C1"
            self.text_color = "#ECEFF4"
            button_font = tkfont.Font(family="Helvetica", size=18)
            button_width = 6
            button_height = 2
        elif mode == "adult":
            self.btn_color = "#4C566A"
            self.btn_color_alt = "#434C5E"
            self.text_color = "#E5E9F0"
            button_font = tkfont.Font(family="Helvetica", size=14)
            button_width = 6
            button_height = 2
        else:  # system
            self.btn_color = "#3B4252"
            self.btn_color_alt = "#4C566A"
            self.text_color = "#E5E9F0"
            button_font = tkfont.Font(family="Helvetica", size=12)
            button_width = 5
            button_height = 2
        
        # Create display frame
        display_frame = tk.Frame(self.root, height=100, bg=self.display_color)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Display for total expression
        total_label = tk.Label(display_frame, textvariable=self.display_var, 
                              anchor="e", bg=self.display_color, fg=self.text_color,
                              font=tkfont.Font(family="Helvetica", size=24))
        total_label.pack(expand=True, fill="both", padx=20, pady=5)
        
        # Create button frame
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('7', '8', '9', '/', '⌫'),
            ('4', '5', '6', 'x', 'C'),
            ('1', '2', '3', '-', '('),
            ('0', '.', '=', '+', ')')
        ]
        
        # Add scientific buttons for system mode
        if mode == "system":
            buttons.insert(0, ('sin', 'cos', 'tan', '^', '√'))
            buttons.insert(1, ('log', 'ln', 'π', 'e', 'Sci'))
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                button = tk.Button(button_frame, text=button_text, font=button_font,
                                 bg=self.btn_color, fg=self.text_color,
                                 command=lambda x=button_text: self.on_button_click(x))
                button.grid(row=i, column=j, padx=5, pady=5, 
                           sticky="nsew", ipadx=button_width, ipady=button_height)
                button_frame.grid_columnconfigure(j, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)
        
        # Add back button
        back_btn = tk.Button(self.root, text="Back", font=button_font,
                           bg=self.btn_color_alt, fg=self.text_color,
                           command=self.create_mode_selection)
        back_btn.pack(pady=10, ipadx=10, ipady=5)
        
        self.update_display()
    
    def on_button_click(self, button_text):
        if button_text == 'C':
            self.current_input = ""
            self.total_expression = ""
        elif button_text == '⌫':
            self.current_input = self.current_input[:-1]
        elif button_text == '=':
            try:
                # Replace special constants
                expression = self.total_expression.replace('π', str(math.pi)).replace('e', str(math.e))
                
                # Handle scientific functions
                if 'sin(' in expression:
                    expression = expression.replace('sin(', 'math.sin(')
                if 'cos(' in expression:
                    expression = expression.replace('cos(', 'math.cos(')
                if 'tan(' in expression:
                    expression = expression.replace('tan(', 'math.tan(')
                if 'log(' in expression:
                    expression = expression.replace('log(', 'math.log10(')
                if 'ln(' in expression:
                    expression = expression.replace('ln(', 'math.log(')
                if '√(' in expression:
                    expression = expression.replace('√(', 'math.sqrt(')
                if '^' in expression:
                    expression = expression.replace('^', '**')
                
                result = str(eval(expression))
                self.total_expression = result
                self.current_input = result
            except Exception:
                self.current_input = "Error"
                self.total_expression = ""
        elif button_text == 'Sci':
            self.scientific_mode = not self.scientific_mode
            self.create_calculator("system")
        else:
            if button_text in ['sin', 'cos', 'tan', 'log', 'ln', '√']:
                self.current_input += button_text + '('
            else:
                self.current_input += str(button_text)
            self.total_expression = self.current_input
        
        self.update_display()
    
    def update_display(self):
        self.display_var.set(self.total_expression)
        if len(self.display_var.get()) > 15:
            display_font = tkfont.Font(family="Helvetica", size=18)
        else:
            display_font = tkfont.Font(family="Helvetica", size=24)
        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and len(widget.winfo_children()) > 0:
                if isinstance(widget.winfo_children()[0], tk.Label):
                    widget.winfo_children()[0].config(font=display_font)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()