




def parse_file(self, filename): #parses the file and creates the dictionary aka our memory
    try:
        with open(filename, 'r') as _data:
            pass
    except FileNotFoundError:
        print("file not found")

def read(self, location):
    """Reads a word from keyboard input then stores that word into memory"""
    newWord = input("Please enter a word! 4 digit signed int")
    self.memDict[location] = newWord

def write(self, location):
    """Prints a word from the given memory location"""
    print(self.memDict[location])
    # Key should be the second half of a given word? Are we passing that or the full word into a function?