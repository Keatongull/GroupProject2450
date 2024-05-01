import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from tkinter import simpledialog, messagebox
from tkinter import ttk
import configparser

class ThemeConfig:

    theme_color = "#0F5132"
    off_color = "#FFFFFF"
    config = None

    @staticmethod
    def change_theme(data_gui):
        top_level_window = data_gui.root.winfo_toplevel()
        new_primary_color = simpledialog.askstring("Change Theme", "Enter the primary color (e.g., #RRGGBB):", parent=top_level_window)
        new_off_color = simpledialog.askstring("Change Theme", "Enter the 'off' color (e.g., #RRGGBB):", parent=top_level_window)
        
        try:
            if new_primary_color:
                data_gui.root.configure(bg=new_primary_color)
                data_gui.left_frame.configure(bg=new_primary_color)
                data_gui.right_frame.configure(bg=new_primary_color)
                data_gui.buttons_frame.configure(bg=new_primary_color)
                data_gui.cwd_frame.configure(bg=new_primary_color)
                ThemeConfig.theme_color = new_primary_color  # Update theme color attribute
            
            if new_off_color:
                ThemeConfig.off_color = new_off_color  # Update off color attribute
            
            ThemeConfig.apply_theme(data_gui)  # Apply the theme
            ThemeConfig.save_config()  # Save theme to config file
            
            # Show success message
            if new_primary_color and new_off_color:
                messagebox.showinfo("Success", f"Theme changed. Primary color: {new_primary_color}, Off color: {new_off_color}")
            elif new_primary_color:
                messagebox.showinfo("Success", f"Primary color changed: {new_primary_color}")
            elif new_off_color:
                messagebox.showinfo("Success", f"Off color changed: {new_off_color}")
            else:
                messagebox.showwarning("No Change", "No color changes applied.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid color or error occurred: {str(e)}")

    @staticmethod
    def apply_theme(data_gui):
        # Apply the theme to the GUI elements
        data_gui.data_entry.configure(bg=ThemeConfig.off_color)  # Set console background color
        
        # Create a style object
        treeview_style = ttk.Style()
        # Set the background color for the Treeview widget
        treeview_style.configure("Treeview", background=ThemeConfig.off_color)
        data_gui.current_dir_text.configure(bg=ThemeConfig.off_color)

    @staticmethod
    def load_config():
        # gets theme from config file
        ThemeConfig.config = configparser.ConfigParser()
        try:
            ThemeConfig.config.read('config.ini')
            ThemeConfig.theme_color = ThemeConfig.config.get('GUI', 'theme_color', fallback='#0F5132')
            ThemeConfig.off_color = ThemeConfig.config.get('GUI', 'off_color', fallback='#FFFFFF')  # Load off color from config
        except Exception as e:
            print("Error loading config:", e)  # Error handling

    @staticmethod
    def save_config():
        # saves theme to config file
        ThemeConfig.config['GUI'] = {'theme_color': ThemeConfig.theme_color, 'off_color': ThemeConfig.off_color}  # Save off color to config
        try:
            with open('config.ini', 'w') as configfile:
                ThemeConfig.config.write(configfile)
            print("Config saved successfully")
        except Exception as e:
            print("Error saving config:", e)  # Error handling