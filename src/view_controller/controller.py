from src.memory.memory import Memory, MemoryStatus
import tkinter as tk
from src.text_file_manager import TextFileManager as TFM
from src.gui.theme_config import ThemeConfig
import os

# from GUI import DataGUI (this line causes a circular import error)

# TODO show the active open file on the UI somewhere

class ViewController:
    def __init__(self, view):
        self.current_memory: Memory = None
        self.view = view
        self.file_address = ""
        self.file_dict = {}

    def run_button_clicked(self):
        # Grabs instruction text from memory editor text box
        # Create the Memory object and start it running
        # Wait for return status
        
        instruction_list = self.view.get_mem_data()
        # if instruction_list is somehow too big, that means the memory editor is bugged
        if len(instruction_list) > Memory.MAX_MEMORY_SIZE:
            self.view.output_to_console("ERROR: instructions lines in editor somehow exceeded max memory size.")
            return
        
        self.current_memory = Memory(instruction_list)
        self.view.output_to_console("\n---- Starting Program Execution ----")

        while True:
            #start memory running
            execution_status = self.current_memory.run_instructions()

            if execution_status == MemoryStatus.HALT:
                # end execution
                self.view.output_to_console("Program Ended Successfully (43 HALT instruction)")
                return
            
            elif execution_status == MemoryStatus.ERROR:
                # print error description, end execution
                self.view.output_to_console(self.current_memory.memory_error.description())
                return

            elif execution_status == MemoryStatus.READ:
                # save user input to memory, resume execution
                user_input = self.view.get_user_input()
                self.current_memory.set_input(user_input)
                continue

            elif execution_status == MemoryStatus.WRITE:
                # print to console, resume execution
                self.view.output_to_console(self.current_memory.get_output())
                continue
            
            else:
                raise Exception("STATUS CODE ERROR")


    def open_button_clicked(self):
        # opens file browser for user to select a text file to open. Inserts file contents to memory editor

        # get the filepath from the file browser
        open_address = TFM.get_file_path_from_browser()
        if open_address == "":
            # the file browser was cancelled
            return
        self.view.clear_wrk_add()

        file_name = self.extract_filename(open_address)
        codeText = TFM.import_text_from_file(open_address)
        instructions = codeText.split('\n')
        if len(instructions) > 250:
            self.view.output_to_console("Error: File contains more than 250 lines")
            return
        
        formatted_instructions = ["0"] * Memory.MAX_MEMORY_SIZE # create empty memory and then fill in instructions
        for i in range(len(instructions)):
            formatted_instructions[i] = instructions[i]

        # set the new file_address after import in case any errors occurred
        self.file_address = open_address
        self.view.update_memory_tree(formatted_instructions)
        self.view.output_wrk_add("Active File " + file_name)
        self.update_file_database(file_name, formatted_instructions)
        self.view.update_file_tree()

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
            self.update_file_database(self.extract_filename(save_address), self.view.get_mem_data())
            self.view.update_file_tree()
            self.view.output_wrk_add("Active File " + self.extract_filename(save_address))
            self.view.output_to_console("File Saved. Active File Set To " + self.file_address)
        else:
            # save to active open file
            code_text = "\n".join(self.view.get_mem_data())
            TFM.export_text_to_file(self.file_address, code_text)
            self.view.output_to_console("File Saved to " + self.file_address)

    def change_theme_button_clicked(self):
        ThemeConfig.change_theme(self.view)

    def extract_filename(self, file_path):
        return os.path.basename(file_path)


    def update_file_database(self, file_name, instructions):
        self.file_dict.update({file_name: instructions})