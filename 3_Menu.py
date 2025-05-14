import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("New", "New File Created")

def open_file():
    messagebox.showinfo("Open", "Opening File...")

def save_file():
    messagebox.showinfo("Save", "File Saved")

def cut_text():
    messagebox.showinfo("Cut", "Cut Selected")

def copy_text():
    messagebox.showinfo("Copy", "Copied to Clipboard")

def paste_text():
    messagebox.showinfo("Paste", "Pasted from Clipboard")

def show_popup(event):
    try:
        popup.tk_popup(event.x_root, event.y_root)
    finally:
        popup.grab_release()

# Main window setup
root = tk.Tk()
root.title("Menu Example - Black & White")
root.geometry("400x300")
root.config(bg="white")

# Menu Bar
menubar = tk.Menu(root, bg="black", fg="white")

# File Menu (Pull-Down)
file_menu = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu (Cascading)
edit_menu = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menubar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu (Simple Item)
help_menu = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Tkinter Menu Demo"))
menubar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menubar)

# Pop-up Menu
popup = tk.Menu(root, tearoff=0, bg="black", fg="white")
popup.add_command(label="Cut", command=cut_text)
popup.add_command(label="Copy", command=copy_text)
popup.add_command(label="Paste", command=paste_text)

# Right-click bind
root.bind("<Button-3>", show_popup)

# Label to demonstrate right-click area
label = tk.Label(root, text="Right-click anywhere for pop-up menu", bg="white", fg="black")
label.pack(expand=True)

root.mainloop()
