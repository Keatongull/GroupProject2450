from memory import Memory
from GUI import DataGUI

def main():

    filename = input("Enter name of file:\n")
    instructionList = []

    try:
        with open(filename, 'r') as _data:
            for _, line in enumerate(_data):
                instructionList.append(line.strip())

        mem = Memory(instructionList)
        mem.runInstructions()

    except FileNotFoundError:
        print("file not found")

    root = tk.Tk()
    app = DataGUI(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
    

if __name__ == "__main__":
    main()