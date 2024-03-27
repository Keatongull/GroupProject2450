import tkinter as tk
from gui import DataGUI

def main():

    root = tk.Tk()
    app = DataGUI(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
    

if __name__ == "__main__":
    main()