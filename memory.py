from memory_commands import Add, Subtract, Divide, Multiply, BranchNeg, BranchZero

class Memory:
    
    def __init__(self, instructionList):
        if len(instructionList) > 100:
            raise Exception("instruction list exceeds memory limit")
        
        # create empty memory and then fill in instructions
        self._memList = ["0"] * 100
        for i in range(len(instructionList)):
            self._memList[i] = instructionList[i]

        #TODO accumulator maybe should be made into an @property and set branch flags when modified

        self._accumulator = 0         # integer used for interal computation
        self._instructionPointer = 0  # points to next location in memory to run
        self._IOAddress = 0           # memory address used for I/O commands

    # called by the ViewController after a WRITE command to get output from memory
    def getOutput(self):
        return self._memList[self._IOAddress]
    
    # called by the ViewController after a READ command to set user input into memory
    def setInput(self, str):
        self._memList[self._IOAddress] = str

    def runInstructions(self):
        """ Loops through instructions in memory executing each one in order
            Returns a status code in case of I/O or halt commands. Or in case of memory or execution error.
            LIST OF STATUS CODES
            - read
            - write
            - halt
            - invalid command error
            - invalid format error
            - memory range error
            - zero division error
        """

        while True:
            # this check is neccessary if there is no HALT instruction present
            if self._instructionPointer < 0 or self._instructionPointer > 99:
                return "memory range error"
            instruction = self._memList[self._instructionPointer]
            #TODO add check for invalid instruction format here

            # parse instruction into command and address parts
            command = instruction[1:3]
            address = int(instruction[3:])
            if address < 0 or address > 99:
                return "memory range error"

            # update next instruction in memory to be run
            self._instructionPointer += 1

            # READ command
            if command == "10":
                # set the memory address that the user input will be set to.
                self._IOAddress = address
                #return "read"
                continue
            
            # WRITE command
            elif command == "11":
                # set the memory address for where the output value is.
                self._IOAddress = address
                #return "write"
                continue

            # LOAD command
            elif command == "20":
                # sets the accumulator value from memory
                self._accumulator = int(self._memList[address])
                continue

            # STORE command
            elif command == "21":
                # saves the accumulator value into memory
                self._memList[address] = str(self._accumulator)
                continue

            # ADD command
            elif command == "30":
                self._accumulator = Add.execute(self._accumulator, int(self._memList[address]))
                continue

            # SUBTRACT command
            elif command == "31":
                self._accumulator = Subtract.execute(self._accumulator, int(self._memList[address]))
                continue

            # DIVID command
            elif command == "32":
                self._accumulator = Divide.execute(self._accumulator, int(self._memList[address]))
                continue

            # MULITPLY command
            elif command == "33":
                self._accumulator = Multiply.execute(self._accumulator, int(self._memList[address]))
                continue

            # BRANCH command
            elif command == "40":
                self._instructionPointer = address
                continue

            # BRANCHNEG command
            elif command == "41":
                if BranchNeg.execute(self._accumulator):
                    self._instructionPointer = address
                continue

            # BRANCHZERO command
            elif command == "42":
                if BranchZero.execute(self._accumulator):
                    self._instructionPointer = address
                continue

            # HALT command
            elif command == "43":
                return "halt"

            else:
                return "invalid command"

        # end instruction loop



    def read(self, location):
        """Reads a word from keyboard input then stores that word into memory"""
        newWord = input("Please enter a word! 4 digit signed int:\n")
        self._memList[location] = newWord

    def write(self, location):
        """Prints a word from the given memory location"""
        print(self._memList[location])
        # Key should be the second half of a given word? Are we passing that or the full word into a function?

    def load(self, location):
        # moves item from memory into the accumulator
        self._accumulator = self._memList[location]

    def store(self, location):
        # store item in accumulator into a memory location
        self._memList[location] = self._accumulator
        