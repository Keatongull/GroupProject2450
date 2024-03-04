import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Tkinter GUI Example")

# Create a label widget
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Click Me", command=display_message)
button.pack()

# Run the event loop
root.mainloop()
