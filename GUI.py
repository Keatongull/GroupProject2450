import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from controller import ViewController

class DataGUI:
    def __init__(self, root):
        self.root = root
        self.viewController = ViewController(self)
        self.root.title("Data Table GUI")
        
        self.left_frame = tk.Frame(self.root, bg='#0F5132')
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root, bg='#0F5132')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        #data entry references the console?
        self.data_entry = tk.Text(self.left_frame, bg='#d3d3d3')
        self.data_entry.pack(fill=tk.BOTH, expand=True, pady=5)
        self.data_entry.bind("<Return>", self.insert_newline)

        self.buttons_frame = tk.Frame(self.left_frame, bg='#0F5132')
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.run_button = tk.Button(self.buttons_frame, text="Run", command=self.viewController.runButtonClicked, width=17, height=2)
        self.run_button.grid(row=0, column=0, padx=5, pady=5)
        self.clear_button = tk.Button(self.buttons_frame, text="Clear", command=self.clear_data, width=17, height=2)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5)
        self.import_button = tk.Button(self.buttons_frame, text="Open File", command=self.viewController.importButtonClicked, width=17, height=2)
        self.import_button.grid(row=0, column=2, padx=5, pady=5)
        self.save_button = tk.Button(self.buttons_frame, text="Save Code", command=self.viewController.saveButtonClicked, width=17, height=2)
        self.save_button.grid(row=0, column=3, padx=5, pady=5)
        self.change_theme_button = tk.Button(self.buttons_frame, text="Change Theme", command=self.change_theme, width=17, height=2)
        self.change_theme_button.grid(row=0, column=4, padx=5, pady=5)
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=root.destroy, width=17, height=2)
        self.exit_button.grid(row=0, column=5, padx=5, pady=5)
        # self.test_button = tk.Button(self.buttons_frame, text="Test", command=self.get_mem_data, width=17, height=2)
        # self.test_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        self.memory_tree = ttk.Treeview(self.right_frame, columns=('Column 1', 'Column 2'), show='headings')
        self.memory_tree.heading('Column 1', text='Line #')
        self.memory_tree.heading('Column 2', text='Memory Editor')
        self.memory_tree.pack(expand=True, fill=tk.BOTH, padx=20)
        self.memory_tree.column('Column 1', width=10, minwidth=30)

        self.update_memory_tree(["0"] * 100)

    def clear_data(self):
        # is this for clearing the console?
        pass

    #updates the memory view with a list of values/instructions
    def update_memory_tree(self, values):
        for row in self.memory_tree.get_children():
            self.memory_tree.delete(row)
        
        for i in range(100):
            instruction = str(values[i]) if i < len(values) else ""
            self.memory_tree.insert('', 'end', value=(i+1, instruction), text=(instruction))

    def insert_newline(self, event):
        self.data_entry.insert(tk.END, "\n")

    def get_mem_data(self):
        mem_data_list = []
        for line in self.memory_tree.get_children():
            mem_data = self.memory_tree.item(line)['text']
            mem_data_list.append(mem_data)
        return mem_data_list


    def change_theme(self):
        hex_value = simpledialog.askstring("Change Theme", "Enter a hex value (e.g., #RRGGBB):")
        if hex_value:
            try:
                self.root.configure(bg=hex_value)
                self.left_frame.configure(bg=hex_value)
                self.right_frame.configure(bg=hex_value)
                self.buttons_frame.configure(bg=hex_value)
                messagebox.showinfo("Success", f"Theme changed to {hex_value}")
            except Exception as e:
                messagebox.showerror("Error", f"Invalid hex value or error occurred: {str(e)}")
