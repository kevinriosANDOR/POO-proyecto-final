import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

messagebox.showinfo("Information", "This is an info message!")

root.destroy()
k