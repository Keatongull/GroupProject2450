from memory import Memory

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
    

if __name__ == "__main__":
    main()