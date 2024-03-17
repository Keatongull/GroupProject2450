from GUI import DataGUI
from memory import Memory
from tkinter import filedialog
import tkinter as tk
from TextFileManager import TextFileManager as TFM

class ViewController:
    def __init__(self, view):
        self.curMemory: Memory = None
        self.view: DataGUI = view
        self.fileAddress = None 

    def runButtonClicked(self):
        # Runs the program
        # Switch statement and loop, similar to runInstructions. Interacts with both memory and gui
        # TODO:
            # Clear the console
            # Take text from memory editor text box
            # Split text on new lines, turn into string list
            # Create the Memory object and start it running
            # Wait for return status
    
        # for line in self.view.tree.get_children():
        #     for value in self.view.tree.item(line)['values']:
        #         print(value)

        memList = []
        if self.fileAddress != None:
            file = open(self.fileAddress, 'r')
            for line in file:
                if len(line.strip()) == 5:
                    memList.append(line.strip())
            file.close()
        print(memList)
        self.curMemory = Memory(memList)

    def importButtonClicked(self):
        # When the import button is clicked this will be called, opens file explorer to select a txt file. Sets our fileAddress
        self.fileAddress = TFM.getFilePathFromBrowser()

    def exportButtonClicked(self):
        # Uses exportText from TFM
        pass 
        # Will reimplement once know where to read data from
        # TFM.exportText(self.fileAddress, text) I'm pulling from tree correct?

    def outputToConsole(self):
        # Outputs text to console, what exactly is this connected to? Our commands?
        # Connected to memory while running, getOutput
        # Append text
        pass

root = tk.Tk()
app = DataGUI(root)
vController = ViewController(app)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

vController.importButtonClicked()
vController.runButtonClicked()
app.memory = vController.curMemory
app.update_table()
root.mainloop()