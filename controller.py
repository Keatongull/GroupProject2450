from GUI import DataGUI
from memory import Memory
from tkinter import filedialog
import tkinter as tk

class ViewController:
    def __init__(self):
        self.curMemory = Memory([])
        self.view = DataGUI(tk.Tk())
        self.fileAddress = None # Will be changed through import button clicked. Is having it set to None by default correct?

    def runButtonClicked(self):
        # Runs the program
        pass
        # TODO:
            # Clear the console
            # Take text from memory editor text box, not currently implemented?
            # Create the Memory object and start it running
            # Wait for return status

    def importButtonClicked(self):
        # When the import button is clicked this will be called, opens file explorer to select a txt file. Sets our fileAddress
        tk.Tk().withdraw()
        self.fileAddress = filedialog.askopenfilename(filetypes=(('Text Files', '*.txt'), )) # Only set it to accept txt files, seem right?

    def exportButtonClicked(self):
        # Saves current file and gives option to rename if desired. Do we want to be able to change the file we save too?
        pass # Will reimplement once know where to read data from
        # new_file = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ))
        # new_file = open(new_file, "w")
        # new_file.write(spot name goes here) # Will read from somewhere on GUI, are we reading from tree or data entry? Probably tree?

    def outputToConsole(self):
        # Outputs text to console, what exactly is this connected to? Our commands?
        pass

    # More needed???

test = ViewController()
test.importButtonClicked()
print(test.fileAddress)


    