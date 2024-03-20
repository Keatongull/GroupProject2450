import tkinter as tk
from tkinter import ttk
from memory import Memory
from controller import ViewController

class DataGUI:
    def __init__(self, root):
        self.root = root
        self.viewController = ViewController(self)
        self.root.title("Data Table GUI")

        self.left_frame = tk.Frame(self.root, bg='#FFFFFF')
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root, bg='#FFFFFF')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.data_entry = tk.Text(self.left_frame, bg='#FFFFFF')
        self.data_entry.pack(fill=tk.BOTH, expand=True, pady=5)
        self.data_entry.bind("<Return>", self.insert_newline)

        self.buttons_frame = tk.Frame(self.left_frame, bg='#4C721D')
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.run_button = tk.Button(self.buttons_frame, text="Run", command=self.viewController.runButtonClicked, width=17, height=2)
        self.run_button.grid(row=0, column=0, padx=5, pady=5)
        self.clear_button = tk.Button(self.buttons_frame, text="Clear", command=self.clear_data, width=17, height=2)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5)
        self.import_button = tk.Button(self.buttons_frame, text="Import Code", command=self.viewController.importButtonClicked, width=17, height=2)
        self.import_button.grid(row=0, column=2, padx=5, pady=5)
        self.save_button = tk.Button(self.buttons_frame, text="Save Code", command=self.viewController.saveButtonClicked, width=17, height=2)
        self.save_button.grid(row=0, column=3, padx=5, pady=5)
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=root.destroy, width=17, height=2)
        self.exit_button.grid(row=0, column=4, columnspan=2, padx=5, pady=5)
        
        self.tree = ttk.Treeview(self.right_frame, columns=('Column 1', 'Column 2'), show='headings')
        self.tree.heading('Column 1', text='Memory Editor')
        self.tree.heading('Column 2', text='Memory Output')
        self.tree.pack(expand=True, fill=tk.BOTH, padx=20)

        self.update_table()

    def clear_data(self):
        # we may not need this functionality anymore.
        pass

    def update_table(self):
        """
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for i, instruction in enumerate(self.memory._memList):
            self.tree.insert('', 'end', values=(i, instruction))
        """

    def insert_newline(self, event):
        self.data_entry.insert(tk.END, "\n")


