from memory import Memory
import tkinter as tk
from TextFileManager import TextFileManager as TFM


class ViewController:
    def __init__(self, view):
        self.current_memory: Memory = None
        self.view = view
        self.file_address = None 

    def _parseFile(self):
        # Goes through the file from fileAddress and creates our new memory instructions
        memList = []
        
        file = open(self.file_address, 'r')
        for line in file:
            if len(line.strip()) == 5: # Only take things that are the correct length
                memList.append(line.strip())
        file.close()
        self.current_memory = Memory(memList) # Sets our current memory as this new memory with our instruction list

    def runButtonClicked(self):
        print("run button clicked")
        
        # Runs the program
        # Switch statement and loop, similar to runInstructions. Interacts with both memory and gui
        # TODO:
            # Clear the console
            # Take text from memory editor text box
            # Split text on new lines, turn into string list
            # Create the Memory object and start it running
            # Wait for return status
        
        while True:
            execution_status = self.current_memory.runInstructions()
            print(execution_status)

            if execution_status == "memory range error":
                break

            elif execution_status == "halt":
                break

            elif execution_status == "read":
                # TODO: Should pause until provided input
                pass

            elif execution_status == "write":
                # TODO: Go fetch the value in the given memory position and print it to console
                pass

            elif execution_status == "invalid command error":
                break
            

    def importButtonClicked(self):
        print("import button clicked")
    
        # When the import button is clicked this will be called, opens file explorer to select a txt file. Sets our fileAddress
        self.file_address = TFM.getFilePathFromBrowser()
        if self.file_address == "":
            # the file browser was cancelled
            return
        code = TFM.importTextFromFile(self.file_address)
        instructions = code.split('\n')
        print(instructions)
        #self.update_table()

    def saveButtonClicked(self):
        print("save button clicked")
    
        # TODO: Will reimplement once know where to read data from
        if self.file_address is None:
            # no code was imported initially, get the new save file
            save_address = TFM.getSaveFilePathFromBrowswer()
            print(save_address)
            # TODO: get text from editor and export it to save_address
        else:
            # TODO: get text from editor and export it to self.fileAddress
            pass
        

    def outputToConsole(self, event):
        # Outputs text to console
        self.view.data_entry.insert(tk.END, event)
        self.view.insert_newline(event)

"""
root = tk.Tk()
app = DataGUI(root)
vController = ViewController(app)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

vController.importButtonClicked()
vController.runButtonClicked()
app.memory = vController.curMemory
app.update_table()
root.mainloop()
"""