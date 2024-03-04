import tkinter as tk
from tkinter import messagebox
from main import all
from memory import all
from memory_commands

def gui():
    name = entry.get()
    message = f"Hello, {name}!"
    display_label.config(text=message)

# Create the main window
root = tk.Tk()
root.title("Tkinter GUI Example")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Create frames for left and right sides
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a label and entry widget on the left frame
label = tk.Label(left_frame, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(left_frame, font=("Arial", 14))
entry.pack(expand=True)

# Create a button widget on the left frame
button = tk.Button(left_frame, text="Greet", command=display_message)
button.pack(pady=10)

# Create a label widget on the right frame
display_label = tk.Label(right_frame, text="", font=("Arial", 18))
display_label.pack(expand=True)

# Run the event loop
root.mainloop()
