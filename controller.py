from memory import Memory
import tkinter as tk
from text_file_manager import TextFileManager as TFM
# from GUI import DataGUI (this line causes a circular import error)


class ViewController:
    def __init__(self, view):
        self.current_memory: Memory = None
        self.view = view
        self.file_address = None 

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

        """
        if self.fileAddress != None:
            instructList = TFM.importText(self.fileAddress).splitlines() # instructlist will be a list made from the contents of the imported file
            # This is really ugly. Iterates through list, making sure each item is the right length, if not we remove it.
            for i in range(len(instructList)):
                if len(instructList[i]) != 5:
                    instructList.pop(i)
        
                    
            self.current_memory = Memory(instructList)
        """
        
        instruct_list = self.view.get_mem_data()
        self.current_memory = Memory(instruct_list)

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
        codeText = TFM.importTextFromFile(self.file_address)
        instructions = codeText.split('\n')
        print(instructions)
        self.view.update_memory_tree(instructions)

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