import tkinter as tk
from tkinter import ttk
from memory import Memory

class DataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Table GUI")
        self.memory = Memory([])

        self.left_frame = tk.Frame(self.root, bg='#FFFFFF')
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root, bg='#FFFFFF')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.data_entry = tk.Text(self.left_frame, bg='#FFFFFF')
        self.data_entry.pack(fill=tk.BOTH, expand=True, pady=5)
        self.data_entry.bind("<Return>", self.insert_newline)

        self.buttons_frame = tk.Frame(self.left_frame, bg='#4C721D')
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.run_button = tk.Button(self.buttons_frame, text="Run", command=self.run, width=17, height=2)
        self.run_button.grid(row=0, column=0, padx=5, pady=5)
        self.clear_button = tk.Button(self.buttons_frame, text="Clear", command=self.clear_data, width=17, height=2)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5)
        self.import_button = tk.Button(self.buttons_frame, text="Import Code", command=self.import_code, width=17, height=2)
        self.import_button.grid(row=0, column=2, padx=5, pady=5)
        self.export_button = tk.Button(self.buttons_frame, text="Export Code", command=self.export_code, width=17, height=2)
        self.export_button.grid(row=0, column=3, padx=5, pady=5)
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=root.destroy, width=17, height=2)
        self.exit_button.grid(row=0, column=4, columnspan=2, padx=5, pady=5)

        self.tree = ttk.Treeview(self.right_frame, columns=('Column 1', 'Column 2'), show='headings')
        self.tree.heading('Column 1', text='Memory 1')
        self.tree.heading('Column 2', text='Memory 2')
        self.tree.pack(expand=True, fill=tk.BOTH, padx=20)

        self.update_table()

    def run(self):
        status = self.memory.runInstructions()
        if status == "halt":
            pass

    def clear_data(self):
        self.memory.clearData()
        self.update_table()

    def import_code(self):
        code = self.data_entry.get("1.0", tk.END)
        instructions = code.split('\n')
        self.memory.loadData(instructions)
        self.update_table()

    def export_code(self):
        pass

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for i, instruction in enumerate(self.memory._memList):
            self.tree.insert('', 'end', values=(i, instruction))

    def insert_newline(self, event):
        self.data_entry.insert(tk.END, "\n")


