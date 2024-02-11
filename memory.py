




def parse_file(self, filename): #parses the file and creates the dictionary aka our memory
    try:
        with open(filename, 'r') as _data:
            pass
    except FileNotFoundError:
        print("file not found")

def read(self, command):
    """Reads a word from keyboard input then stores that word into memory"""
    newWord = input("Please enter a word! 4 digit signed int")
    self.memDict[key] = newWord

def write(self, command):
    """Prints a word from the given memory location"""
    print(self.memDict[key]) # Key should be the second half of a given word?