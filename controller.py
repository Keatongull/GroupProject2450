from GUI import DataGUI
from memory import Memory
from tkinter import filedialog
import tkinter as tk
from TextFileManager import TextFileManager as TFM

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
        self.fileAddress = TFM.getFilePathFromBrowser()

    def exportButtonClicked(self):
        # Uses exportText from TFM
        pass # Will reimplement once know where to read data from
        # TFM.exportText(self.fileAddress, text) I'm pulling from tree correct?

    def outputToConsole(self):
        # Outputs text to console, what exactly is this connected to? Our commands?
        pass

    # More needed???

test = ViewController()
test.importButtonClicked()
print(test.fileAddress)


    