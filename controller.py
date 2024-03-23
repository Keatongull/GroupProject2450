from memory import Memory
import tkinter as tk
from text_file_manager import TextFileManager as TFM
# from GUI import DataGUI (this line causes a circular import error)

# TODO show the active open file on the UI somewhere

class ViewController:
    def __init__(self, view):
        self.current_memory: Memory = None
        self.view = view
        self.file_address = ""

    def run_button_clicked(self):
        # TODO Clear the console
        # Grabs instruction text from memory editor text box
        # Create the Memory object and start it running
        # Wait for return status
        
        instruction_list = self.view.get_mem_data()
        # stop program from running if memory is too large
        if len(instruction_list) > 100:
            self.view.output_to_console("Runtime memory cannot exceed 100 instructions. Please remove excess lines from editor and try again.")
            return
        
        self.current_memory = Memory(instruction_list)

        while True:
            #start memory running
            execution_status = self.current_memory.run_instructions()

            if execution_status == "halt":
                # end execution
                self.view.output_to_console("\nProgram Ended (status 43 : HALT command)")
                return

            elif execution_status == "read":
                user_input = self.view.get_user_input()
                self.current_memory.set_input(user_input)
                continue

            elif execution_status == "write":
                self.view.output_to_console(self.current_memory.get_output())
                continue

            elif execution_status == "memory range error":
                # end execution
                self.view.output_to_console("\nProgram Ended (status : memory range error)")
                return
            
            elif execution_status == "command format error":
                # end execution
                self.view.output_to_console("\nProgram Ended (status : commmand format error)")
                return
            
            else:
                raise Exception("STATUS CODE ERROR")
            

    def open_button_clicked(self):
        # opens file browser for user to select a text file to open. Inserts file contents to memory editor
        open_address = TFM.get_file_path_from_browser()
        if open_address == "":
            # the file browser was cancelled
            return
        
        codeText = TFM.import_text_from_file(open_address)
        instructions = codeText.split('\n')
        # set the new file_address after import in case any errors occurred
        self.file_address = open_address
        self.view.update_memory_tree(instructions)
        self.view.output_to_console("Active File Set To " + open_address)

    def save_button_clicked(self):
        # saves to the active open file, otherwise asks create a new file, then sets it as active
    
        if self.file_address == "":
            # no file was currently open, save to a new file instead
            save_address = TFM.get_save_file_path_from_browser()
            if save_address == "":
                # file browser was cancelled
                return
            code_text = "\n".join(self.view.get_mem_data())
            TFM.export_text_to_file(save_address, code_text)
            # open the new file
            self.file_address = save_address
            self.view.output_to_console("File Saved. Active File Set To " + self.file_address)
        else:
            # save to active open file
            code_text = "\n".join(self.view.get_mem_data())
            TFM.export_text_to_file(self.file_address, code_text)
            self.view.output_to_console("File Saved to " + self.file_address)
        