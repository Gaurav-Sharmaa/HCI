import tkinter as tk

class WindowDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Demo Screens - HCI Lab")
        self.root.configure(bg="white")
        
        # Set up the main window
        self.root.geometry("600x400")
        
        # Create header and title
        header = tk.Frame(self.root, bg="black", height=25)
        header.pack(fill="x")
        
        tk.Label(self.root, text="Primary Window", font=("Arial", 12, "bold"), bg="white").pack(pady=10)
        
        # Create a list of all button options and their corresponding functions
        # Each tuple contains (button text, function to call when clicked)
        buttons = [
            ("Open Dialog Box", self.open_dialog_box),
            ("Open Property Sheet", self.open_property_sheet),
            ("Open Property Inspector", self.open_property_inspector),
            ("Open Message Box", self.open_message_box),
            ("Open Palette Window", self.open_palette_window),
            ("Open Pop-up Window", self.open_popup_window)
        ]
        
        # Create all buttons automatically from the list above
        # This avoids having to write repetitive code for each button
        for text, command in buttons:
            tk.Button(self.root, text=text, command=command, bg="white", width=20).pack(pady=3)

    def create_window(self, title, size="300x150"):
        """Helper function to create standard window with header"""
        # Create a new window that's connected to the main window (parent-child relationship)
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry(size)  # Set window dimensions (width x height)
        win.configure(bg="white")
        
        # Add a black header bar at the top of each window for consistent design
        header = tk.Frame(win, bg="black", height=25)
        header.pack(fill="x")  # Make the header stretch across the full width
        tk.Label(header, text=title, fg="white", bg="black").pack(anchor="w", padx=5)
        
        return win

    def open_dialog_box(self):
        win = self.create_window("Dialog Box")
        tk.Label(win, text="This is a Dialog Box", bg="white", pady=20).pack()
        tk.Button(win, text="OK", command=win.destroy, width=10, bg="white").pack()

    def open_property_sheet(self):
        win = self.create_window("Property Sheet", "300x200")
        
        tk.Label(win, text="Property Sheet Example", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
        
        frame = tk.Frame(win, bg="white")
        frame.pack(fill="x", padx=20, pady=5)
        tk.Label(frame, text="Property 1:", bg="white").pack(side="left")
        tk.Entry(frame).pack(side="left", fill="x", expand=True)
        
        btn_frame = tk.Frame(win, bg="white")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="OK", command=win.destroy, width=8).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=win.destroy, width=8).pack(side="left")

    def open_property_inspector(self):
        win = self.create_window("Property Inspector", "300x200")
        
        tk.Label(win, text="Property Inspector", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
        
        # Create multiple property fields dynamically using a loop
        # This creates Property 1 and Property 2 with their respective text input fields
        for i in range(1, 3):
            frame = tk.Frame(win, bg="white")
            frame.pack(fill="x", padx=20, pady=5)
            tk.Label(frame, text=f"Property {i}:", bg="white").pack(side="left")
            tk.Entry(frame).pack(side="left", fill="x", expand=True)
        
        tk.Button(win, text="Apply", command=win.destroy, width=8).pack(pady=10)

    def open_message_box(self):
        win = self.create_window("Message Box")
        tk.Label(win, text="This is a message box", bg="white", pady=20).pack()
        tk.Button(win, text="OK", command=win.destroy, width=10).pack()

    def open_palette_window(self):
        win = self.create_window("Palette Window")
        
        tk.Label(win, text="Choose an Option:", bg="white").pack(pady=5)
        
        tk.Button(win, text="", width=3, height=1, bg="white", 
                 command=lambda: self.open_palette_option("Option 1")).pack(pady=5)
        tk.Button(win, text="", width=3, height=1, bg="white",
                 command=lambda: self.open_palette_option("Option 2")).pack(pady=5)

    def open_palette_option(self, option):
        win = self.create_window("Palette's option", "250x120")
        tk.Label(win, text=f"You selected {option}", bg="white", pady=20).pack()
        tk.Button(win, text="OK", command=win.destroy, width=10).pack()

    def open_popup_window(self):
        # Create a special type of window that appears on top of everything else
        popup = tk.Toplevel(self.root)
        popup.title("Pop-up Window")
        popup.geometry("250x120")
        popup.configure(bg="white")
        # Remove standard window borders and title bar to make it look like a true popup
        popup.overrideredirect(True)  # This removes all window decorations
        
        # Position popup relative to main window (100 pixels to the right and down)
        # This ensures the popup appears near the main window instead of at a random location
        popup.geometry(f"+{self.root.winfo_x() + 100}+{self.root.winfo_y() + 100}")
        
        # Create a frame with a black border to make the popup look like a floating panel
        frame = tk.Frame(popup, bg="white", highlightbackground="black", highlightthickness=1)
        frame.pack(fill="both", expand=True)
        
        tk.Label(frame, text="This is a Pop-up Window", bg="white", pady=20).pack()
        tk.Button(frame, text="Close", command=popup.destroy, width=10).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = WindowDemoApp(root)
    root.mainloop()