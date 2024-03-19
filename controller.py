from GUI import DataGUI
from memory import Memory
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

        if self.fileAddress != None:
            instructList = TFM.importText(self.fileAddress).splitlines() # instructlist will be a list made from the contents of the imported file
            # This is really ugly. Iterates through list, making sure each item is the right length, if not we remove it.
            for i in range(len(instructList)):
                if len(instructList[i]) != 5:
                    instructList.pop(i)

            self.curMemory = Memory(instructList)
        
        while True:
            curInstruction = self.curMemory.runInstructions()
            self.outputToConsole(curInstruction)
            # print(curInstruction)

            if curInstruction == "memory range error":
                break

            elif curInstruction == "halt":
                break

            elif curInstruction == "read":
                # TODO: Should pause until provided input
                pass

            elif curInstruction == "write":
                # TODO: Go fetch the value in the given memory position and print it to console
                pass

            elif curInstruction == "invalid command error":
                break
            

    def importButtonClicked(self):
        # When the import button is clicked this will be called, opens file explorer to select a txt file. Sets our fileAddress
        self.fileAddress = TFM.getFilePathFromBrowser()

    def exportButtonClicked(self):
        # Uses exportText from TFM
        pass 
        # TODO: Will reimplement once know where to read data from
        # TFM.exportText(self.fileAddress, text) I'm pulling from tree correct?

    def outputToConsole(self, event):
        # Outputs text to console
        self.view.data_entry.insert(tk.END, event)
        self.view.insert_newline(event)

root = tk.Tk()
app = DataGUI(root)
vController = ViewController(app)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

vController.importButtonClicked()
vController.runButtonClicked()
app.memory = vController.curMemory
app.update_table()
root.mainloop()