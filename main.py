from memory import Memory

memory = Memory()

def main():
    filename = input("Enter name of file:\n")
    memory.parse_file(filename)



if __name__ == "__main__":
    main()