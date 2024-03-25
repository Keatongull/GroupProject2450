from memory_commands import Add, Subtract, Divide, Multiply, BranchNeg, BranchZero

# TODO create memory error object for detailed error messages
# TODO add operand type error checking for all commands
# TODO write constants for commands and status codes

class Memory:
    
    # requires a string list of commands to initialize
    def __init__(self, instructionList):
        if len(instructionList) > 100:
            raise Exception("instruction list exceeds memory limit")
        
        # create empty memory and then fill in instructions
        self._memory_list = ["0"] * 100
        for i in range(len(instructionList)):
            self._memory_list[i] = instructionList[i]

        self._accumulator = 0         # integer used for internal computation
        self._instruction_pointer = 0  # points to next location in memory to run
        self._IO_address = 0           # memory address used for I/O commands



    def get_output(self):
        # called by the ViewController after a WRITE command to get output from memory
        return self._memory_list[self._IO_address - 1]
    

    
    def set_input(self, str):
        # called by the ViewController after a READ command to set user input into memory
        self._memory_list[self._IO_address - 1] = str



    def run_instructions(self):
        """ Loops through instructions in memory executing each one in order
            Returns a status code in case of I/O or halt commands. Or in case of memory or execution error.
            LIST OF STATUS CODES
            - read
            - write
            - halt
            - command format error
            - memory range error
            - zero division error
        """
        
        # begin loop of memory execution
        while True:
            # this check is neccessary if there is no HALT instruction present
            if self._instruction_pointer < 0 or self._instruction_pointer > 99:
                return "memory range error"
            instruction = self._memory_list[self._instruction_pointer]

            #TODO add a regex to check for invalid instruction format here
            if len(instruction) != 5:
                return "command format error"

            # parse instruction into command and address parts
            command = instruction[1:3]
            # rememeber that addresses are 1 based but the memory list is zero based
            address = int(instruction[3:])

            if command != "43" and (address < 1 or address > 100):
                return "memory range error"

            # update next instruction in memory to be run
            self._instruction_pointer += 1

            # READ command
            if command == "10":
                # set the memory address that the user input will be set to.
                self._IO_address = address
                return "read"
            
            # WRITE command
            elif command == "11":
                # set the memory address for where the output value is.
                self._IO_address = address
                return "write"

            # LOAD command
            elif command == "20":
                # sets the accumulator value from memory
                self._accumulator = int(self._memory_list[address - 1])
                continue

            # STORE command
            elif command == "21":
                # saves the accumulator value into memory
                self._memory_list[address - 1] = str(self._accumulator)
                continue

            # ADD command
            elif command == "30":
                self._accumulator = Add.execute(self._accumulator, int(self._memory_list[address]))
                continue

            # SUBTRACT command
            elif command == "31":
                self._accumulator = Subtract.execute(self._accumulator, int(self._memory_list[address]))
                continue

            # DIVIDE command
            elif command == "32":
                try:
                    self._accumulator = Divide.execute(self._accumulator, int(self._memory_list[address]))
                except ZeroDivisionError:
                    return "zero division error"
                continue

            # MULITPLY command
            elif command == "33":
                self._accumulator = Multiply.execute(self._accumulator, int(self._memory_list[address]))
                continue

            # BRANCH command
            elif command == "40":
                self._instruction_pointer = address
                continue

            # BRANCHNEG command
            elif command == "41":
                if BranchNeg.execute(self._accumulator):
                    self._instruction_pointer = address
                continue

            # BRANCHZERO command
            elif command == "42":
                if BranchZero.execute(self._accumulator):
                    self._instruction_pointer = address
                continue

            # HALT command
            elif command == "43":
                return "halt"

            else:
                return "command format error"

        # end execution loop
        