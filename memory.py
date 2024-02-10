




def parse_file(self, filename): #parses the file and creates the dictionary aka our memory
    try:
        with open(filename, 'r') as _data:
            pass
    except FileNotFoundError:
        print("file not found")