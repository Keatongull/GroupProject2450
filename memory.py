class memory:
    def __init__(self) -> None:
        self.memDict = {}
        self.accumulator = 0

    def parse_file(self, filename): #parses the file and creates the dictionary aka our memory
        try:
            with open(filename, 'r') as _data:
                for i, line in enumerate(file):
                    if i < 100:
                        self.memDict[i] = int(line.strip())
                    else:
                        print("Warning: Program size exceeds memory capacity. Ignoring additional lines.")
                        break
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

    def load(self, location):
        #moves item from memory into the accumulator
        accumulator = self.memDict[location]

    def store(self, location):
        #store item in accumulator into a memory location
        self.memDict[location] = self.accumulator
        