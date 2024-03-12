from tkinter import filedialog

class TextFileManager:
    @staticmethod
    def exportText(filename, text):
        try:
            if filename == "":
                raise ValueError
            with open(filename, 'w') as write_file:
                write_file.write(text)

        except ValueError:
            print("export file must have a name")

    @staticmethod
    def importText(filename):
        try:
            with open(filename, 'r') as read_file:
                content = read_file.read()
                return content
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def getFilePathFromBrowser():
        # if the file browser is cancelled, returns an empty string
        name = filedialog.askopenfilename(initialdir="/", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
        return name