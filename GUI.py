import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import configparser
from controller import ViewController

class DataGUI:
    def __init__(self, root):
        self.root = root
        self.viewController = ViewController(self)
        self.root.title("Data Table GUI")
        
        self.load_config()  # Load theme from config file

        self.left_frame = tk.Frame(self.root, bg=self.theme_color)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.right_frame = tk.Frame(self.root, bg=self.theme_color)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)


        # Data entry references the console
        self.data_entry = tk.Text(self.left_frame, bg=self.off_color)
        self.data_entry.pack(fill=tk.BOTH, expand=True, pady=5)
        self.data_entry.bind("<Return>", self.insert_newline_in_console)

        self.buttons_frame = tk.Frame(self.left_frame, bg=self.theme_color)
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
        self.edit_cell_button.grid(row=0, column=4, padx=5, pady=6)
        self.change_theme_button = tk.Button(self.buttons_frame, text="Change Theme", command=self.change_theme, width=17, height=2)
        self.change_theme_button.grid(row=0, column=5, padx=5, pady=5)
        self.exit_button = tk.Button(self.buttons_frame, text="Exit", command=root.destroy, width=17, height=2)
        self.exit_button.grid(row=0, column=6, padx=5, pady=5)

        self.memory_tree = ttk.Treeview(self.right_frame, columns=('Column 1', 'Column 2'), show='headings')
        self.memory_tree.heading('Column 1', text='Line #')
        self.memory_tree.heading('Column 2', text='Memory Editor')
        self.memory_tree.pack(expand=True, fill=tk.BOTH, padx=20)
        self.memory_tree.column('Column 1', width=10, minwidth=30)

        self.update_memory_tree(["0"] * 100)

    def clear_console(self):
        self.data_entry.delete('1.0', tk.END)


    def edit_cell(self):
        selected_item = self.memory_tree.focus()

        if selected_item:
            current_line = self.memory_tree.item(selected_item, 'values')[0]
            current_value = self.memory_tree.item(selected_item, 'values')[1]

            new_value = simpledialog.askstring("Edit Cell", "Enter new value:", initialvalue=current_value)

            if new_value is not None:
                self.memory_tree.item(selected_item, values=(current_line, new_value), text=new_value)
                messagebox.showinfo("Success", "Cell updated successfully.")
                self.get_mem_data()
        else:
            messagebox.showwarning("Warning", "Please select a cell to edit.")



    #updates the memory view with a list of values/instructions
    def update_memory_tree(self, values):
        for row in self.memory_tree.get_children():
            self.memory_tree.delete(row)
        
        for i in range(100):
            instruction = str(values[i]) if i < len(values) else ""
            self.memory_tree.insert('', 'end', value=(i+1, instruction), text=(instruction))

    def insert_newline_in_console(self):
        self.data_entry.insert(tk.END, "\n")

    def output_to_console(self, text):
        # Outputs text to console
        self.data_entry.insert(tk.END, text)
        self.insert_newline_in_console()

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

    def change_theme(self):
        top_level_window = self.root.winfo_toplevel()
        primary_color = simpledialog.askstring("Change Theme", "Enter the primary color (e.g., #RRGGBB):", parent=top_level_window)
        off_color = simpledialog.askstring("Change Theme", "Enter the 'off' color (e.g., #RRGGBB):", parent=top_level_window)
        
        try:
            if primary_color:
                self.root.configure(bg=primary_color)
                self.left_frame.configure(bg=primary_color)
                self.right_frame.configure(bg=primary_color)
                self.buttons_frame.configure(bg=primary_color)
                self.theme_color = primary_color  # Update theme color attribute
            
            if off_color:
                self.off_color = off_color  # Update off color attribute
            
            self.apply_theme()  # Apply the theme
            self.save_config()  # Save theme to config file
            
            # Show success message
            if primary_color and off_color:
                messagebox.showinfo("Success", f"Theme changed. Primary color: {primary_color}, Off color: {off_color}")
            elif primary_color:
                messagebox.showinfo("Success", f"Primary color changed: {primary_color}")
            elif off_color:
                messagebox.showinfo("Success", f"Off color changed: {off_color}")
            else:
                messagebox.showwarning("No Change", "No color changes applied.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid color or error occurred: {str(e)}")


    def apply_theme(self):
        # Apply the theme to the GUI elements
        self.data_entry.configure(bg=self.off_color)  # Set console background color
        # You can continue setting other widgets to the off color as needed

    def load_config(self):
        # gets theme from config file
        self.config = configparser.ConfigParser()
        try:
            self.config.read('config.ini')
            self.theme_color = self.config.get('GUI', 'theme_color', fallback='#0F5132')
            self.off_color = self.config.get('GUI', 'off_color', fallback='#FFFFFF')  # Load off color from config
        except Exception as e:
            print("Error loading config:", e)  # Error handling

    def save_config(self):
        # saves theme to config file
        self.config['GUI'] = {'theme_color': self.theme_color, 'off_color': self.off_color}  # Save off color to config
        try:
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            print("Error saving config:", e)  # Error handling
