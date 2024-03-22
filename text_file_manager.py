from tkinter import filedialog

class TextFileManager:

    @staticmethod
    def export_text_to_file(filename, text):
        # writes contents of a string to a specified file
        # creates the file if it doesn't already exist
        try:
            if filename == "":
                raise ValueError
            with open(filename, 'w') as write_file:
                write_file.write(text)

        except ValueError:
            print("export file must have a name")

    @staticmethod
    def import_text_from_file(filename):
        # returns a string of text read from the specified file
        try:
            with open(filename, 'r') as read_file:
                content = read_file.read()
                return content
        except FileNotFoundError:
            print("file not found")
            return ""

    @staticmethod
    def get_file_path_from_browser():
        # opens file browser and returns the filepath
        # if the file browser is cancelled, returns an empty string
        file_address = filedialog.askopenfilename(initialdir="/", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        return file_address
    
    @staticmethod
    def get_save_file_path_from_browser():
        # asks user to create a new file with .txt extenstion, returns the filepath, or empty string if cancelled
        file_address = filedialog.asksaveasfile(initialdir="/", defaultextension=".txt")
        # asksaveasfile returns a TextIOWrapper object. Returns None if operation is cancelled
        if file_address is None:
            return ""
        return file_address.name