def parse_file(self, filename):
    try:
        with open(filename, 'r') as _data:
            pass
    except FileNotFoundError:
        print("file not found")