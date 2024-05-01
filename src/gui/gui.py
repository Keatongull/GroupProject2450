import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from src.view_controller.controller import ViewController
from src.memory.memory import Memory
from src.gui.theme_config import ThemeConfig

class DataGUI:
    def __init__(self, root):
        self.root = root
        self.viewController = ViewController(self)
        self.root.title("Data Table GUI")
        #self.theme_color = '#0F5132'
        ThemeConfig.theme_color = "#0F5132"
        #self.off_color = '#FFFFFF'
        ThemeConfig.off_color = "#FFFFFF"
        self.item_text = ''
        
        ThemeConfig.load_config()  # Load theme from config file
        self.root['bg'] = ThemeConfig.theme_color

        self.left_frame = tk.Frame(self.root, bg=ThemeConfig.theme_color)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root, bg=ThemeConfig.theme_color)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.cwd_frame = tk.Frame(self.left_frame, bg=ThemeConfig.theme_color)
        self.cwd_frame.pack(anchor="w", padx=5, pady=5)

        self.current_dir_text = tk.Text(self.cwd_frame, height=1, bg=ThemeConfig.off_color, width=119)
        self.current_dir_text.pack(fill=tk.X, padx=5)


        # Data entry references the console
        self.data_entry = tk.Text(self.left_frame, bg=ThemeConfig.off_color)
        self.data_entry.pack(fill=tk.BOTH, expand=True, pady=5)
        self.data_entry.bind("<Return>", self.insert_newline_in_console)

        self.buttons_frame = tk.Frame(self.left_frame, bg=ThemeConfig.theme_color)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.run_button = tk.Button(self.buttons_frame, text="Run", command=self.viewController.run_button_clicked, width=17, height=2)
        self.run_button.grid(row=0, column=0, padx=5, pady=5)
        self.clear_button = tk.Button(self.buttons_frame, text="Clear Console", command=self.clear_console, width=17, height=2)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5)
        self.import_button = tk.Button(self.buttons_frame, text="Open File", command=self.viewController.open_button_clicked, width=17, height=2)
        self.import_button.grid(row=0, column=2, padx=5, pady=5)
        self.save_button = tk.Button(self.buttons_frame, text="Save Code", command=self.viewController.save_button_clicked, width=17, height=2)
        self.save_button.grid(row=0, column=3, padx=5, pady=5)
        self.edit_cell_button = tk.Button(self.buttons_frame, text="Edit Memory", command=self.edit_cell, width=17, height=2)
        self.edit_cell_button.grid(row=1, column=0, padx=5, pady=6)
        self.change_theme_button = tk.Button(self.buttons_frame, text="Change Theme", command=self.viewController.change_theme_button_clicked, width=17, height=2)
        self.change_theme_button.grid(row=1, column=1, padx=5, pady=5)
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=root.destroy, width=17, height=2)
        self.exit_button.grid(row=1, column=2, padx=5, pady=5)

        self.memory_tree = ttk.Treeview(self.right_frame, columns=('Column 1', 'Column 2'), show='headings')
        self.memory_tree.heading('Column 1', text='Line #')
        self.memory_tree.heading('Column 2', text='Memory Editor')
        self.memory_tree.pack(expand=True, fill=tk.BOTH, padx=20)
        self.memory_tree.column('Column 1', width=10, minwidth=30)

        self.file_tree = ttk.Treeview(self.left_frame, columns=('Column1'), show='headings', height=5)
        self.file_tree.column('Column1', width=10)  # Adjust the width as needed
        self.file_tree.heading('Column1', text='Open Files')
        self.file_tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=20, anchor=tk.CENTER)
        self.file_tree.bind("<<TreeviewSelect>>", self.open_file_selected)

        self.update_memory_tree(["0"] * Memory.MAX_MEMORY_SIZE)

    def clear_console(self):
        self.data_entry.delete('1.0', tk.END)

    def clear_wrk_add(self):
        self.current_dir_text.delete('1.0', tk.END)


    def edit_cell(self):
        selected_item = self.memory_tree.focus()

        if selected_item:
            current_line = self.memory_tree.item(selected_item, 'values')[0]
            current_value = self.memory_tree.item(selected_item, 'values')[1]

            new_value = simpledialog.askstring("Edit Cell", "Enter new value:", initialvalue=current_value)

            #check if user cancelled
            if new_value is not None:
                self.memory_tree.item(selected_item, values=(current_line, new_value), text=new_value)
                #do not update file_dict if there is not an active file
                if self.viewController.file_address != "":
                    self.viewController.file_dict.update({self.viewController.extract_filename(self.viewController.file_address): self.get_mem_data()})

        else:
            messagebox.showwarning("Warning", "Please select a cell to edit.")

    def update_file_tree(self):
        self.file_tree.delete(*self.file_tree.get_children())
        for _key in self.viewController.file_dict.keys():
            self.file_tree.insert('', 'end', values=_key)



    #updates the memory view with a list of values/instructions
    def update_memory_tree(self, values):
        for row in self.memory_tree.get_children():
            self.memory_tree.delete(row)
        
        for i in range(Memory.MAX_MEMORY_SIZE):
            instruction = str(values[i]) if i < len(values) else ""
            self.memory_tree.insert('', 'end', value=(i+1, instruction), text=(instruction))

    def insert_newline_in_console(self):
        self.data_entry.insert(tk.END, "\n")

    def output_to_console(self, text):
        # Outputs text to console
        self.data_entry.insert(tk.END, text)
        self.insert_newline_in_console()

    def output_wrk_add(self, text):
        self.clear_wrk_add()
        filename = self.viewController.extract_filename(text)
        self.current_dir_text.insert(tk.END, filename)


    def get_mem_data(self):
        mem_data_list = []
        for line in self.memory_tree.get_children():
            mem_data = self.memory_tree.item(line)['text']
            if mem_data == "":
                mem_data_list.append("0")
            else:
                mem_data_list.append(mem_data)
        return mem_data_list
    
    def get_user_input(self):
        # called during a READ command. Returns a string of user input.
        text = simpledialog.askstring("User Input Expected", "Enter Text")
        # askstring returns None if cancelled
        if text is None:
            return ""
        return text

    def open_file_selected(self, event=None):
        if self.file_tree.selection():
            selected_item = self.file_tree.selection()
            self.item_text = self.file_tree.item(selected_item)['values']
            # Clear existing entries in the memory tree
            for row in self.memory_tree.get_children():
                self.memory_tree.delete(row)
            # Find the selected file in the list of dictionaries
                #if file == item_text[0]:
                # Update the memory tree with instructions from the selected file
            self.update_memory_tree(self.viewController.file_dict.get(self.item_text[0]))
            self.output_wrk_add(f'Active file set to: {self.item_text[0]}')