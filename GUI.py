import tkinter as tk
from tkinter import ttk
from memory import Memory

class DataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UVSimulator GUI")
        self.memory = Memory([])  # Create an instance of the Memory class

        # Create frames
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create text entry for inputting the program
        self.program_entry_label = tk.Label(self.left_frame, text="Enter program:")
        self.program_entry_label.pack(fill=tk.X)
        self.program_entry = tk.Text(self.left_frame, height=10)
        self.program_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        # Create buttons
        self.buttons_frame = tk.Frame(self.left_frame)
        self.buttons_frame.pack(fill=tk.X, padx=5, pady=5)

        self.run_button = tk.Button(self.buttons_frame, text="Run Program", command=self.run_program)
        self.run_button.pack(side=tk.LEFT, padx=5)
        self.clear_button = tk.Button(self.buttons_frame, text="Clear Output", command=self.clear_output)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Create text widget for program output
        self.output_text = tk.Text(self.right_frame)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def run_program(self):
        program_text = self.program_entry.get(1.0, tk.END)  # Get program text from the text entry
        program_lines = program_text.split('\n')
        self.memory.loadProgramFromLines(program_lines)  # Load program into memory

        status = self.memory.runInstructions()  # Run the program

        if status == "read":
            input_value = input("Enter a word: ")
            self.memory.setInput(input_value)
        elif status == "write":
            output_value = self.memory.getOutput()
            self.output_text.insert(tk.END, output_value + "\n")
        elif status == "halt":
            self.output_text.insert(tk.END, "Program halted.\n")
        elif status == "invalid command":
            self.output_text.insert(tk.END, "Invalid command.\n")
        elif status == "memory range error":
            self.output_text.insert(tk.END, "Memory range error.\n")
        elif status == "zero division error":
            self.output_text.insert(tk.END, "Zero division error.\n")

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataGUI(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
