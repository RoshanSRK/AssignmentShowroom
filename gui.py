import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("UiPath Python GUI", "Hello from Python!")

def start_gui():
    root = tk.Tk()
    root.title("UiPath Python GUI")
    
    button = tk.Button(root, text="Click Me", command=show_message)
    button.pack(pady=20)
    
    root.mainloop()
