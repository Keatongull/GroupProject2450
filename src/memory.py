from memory_instructions import InstructionType, Add, Subtract, Divide, Multiply, BranchNeg, BranchZero
from memory_error import MemoryError, MemoryErrorType as MET
import re
from enum import Enum

# TODO add operand type error checking for all instructions

class MemoryStatus(Enum):
    # status codes returned by memory when execution is paused
    READ = "read"
    WRITE = "write"
    HALT = "halt"
    ERROR = "error"


class Memory:

    MAX_MEMORY_SIZE = 250  # the maximum amount of lines in memory.
    
    # requires a string list of instructions to initialize
    def __init__(self, instructionList):
        assert len(instructionList) <= Memory.MAX_MEMORY_SIZE

        #Public Properties
        self.memory_error = None   # contains the error object when an error status is returned

        # Private Properties
        self._memory_list = ["0"] * Memory.MAX_MEMORY_SIZE # create empty memory and then fill in instructions
        for i in range(len(instructionList)):
            self._memory_list[i] = instructionList[i]
        self._accumulator = 0          # integer used for internal computation
        self._instruction_pointer = 0  # points to next location in memory to run
        self._IO_address = 0           # memory address used for I/O instruction_types

        # determine instruction length by checking the first instruction
        # set instruction_regex for validating 5 or 6 length instructions only
        if len(self._memory_list[0]) == 5:
            self._instruction_regex = "^[+](([1][0-1])|([2][0-1])|([3][0-3])|([4][0-3]))\d\d$"
        else:
            self._instruction_regex = "^[+](([1][0-1])|([2][0-1])|([3][0-3])|([4][0-3]))\d\d\d$"
        


    def get_output(self):
        # called by the ViewController after a WRITE instruction to get output from memory
        return self._memory_list[self._IO_address - 1]
    

    
    def set_input(self, str):
        # called by the ViewController after a READ instruction to set user input into memory
        self._memory_list[self._IO_address - 1] = str



    def run_instructions(self):
        # Loops through instructions in memory executing each one in order
        # Returns a memory status for I/O instruction, halt instruction, or execution error.

        # begin loop of memory execution
        while True:
            # this check is neccessary if there is no HALT instruction present
            if self._instruction_pointer < 0 or self._instruction_pointer > Memory.MAX_MEMORY_SIZE - 1:
                self.memory_error = MemoryError(MET.MEMORY_RANGE)
                return MemoryStatus.ERROR
            instruction = self._memory_list[self._instruction_pointer]

            # check formatting of the instruction using regex
            if re.search(self._instruction_regex, instruction) is None:
                    self.memory_error = MemoryError(MET.INSTRUCTION_FORMAT, self._instruction_pointer + 1, instruction)
                    return MemoryStatus.ERROR
            
            # parse instruction into operation and address parts
            instruction_type = instruction[1:3]
            # rememeber that addresses are 1 based but the memory list is zero based
            instruction_address = int(instruction[3:])

            # check that instruction_address is in memory range
            if instruction_type != InstructionType.HALT.value and (instruction_address < 1 or instruction_address > Memory.MAX_MEMORY_SIZE):
                self.memory_error = MemoryError(MET.INSTRUCTION_RANGE, self._instruction_pointer + 1, instruction)
                return MemoryStatus.ERROR

            # update next instruction in memory to be run
            self._instruction_pointer += 1

            # READ instruction
            if instruction_type == InstructionType.READ.value:
                # set the memory address that the user input will be set to.
                self._IO_address = instruction_address
                return MemoryStatus.READ
            
            # WRITE instruction
            elif instruction_type == InstructionType.WRITE.value:
                # set the memory address for where the output value is.
                self._IO_address = instruction_address
                return MemoryStatus.WRITE

            # LOAD instruction
            elif instruction_type == InstructionType.LOAD.value:
                # sets the accumulator value from memory
                self._accumulator = int(self._memory_list[instruction_address - 1])
                continue

            # STORE instruction
            elif instruction_type == InstructionType.STORE.value:
                # saves the accumulator value into memory
                self._memory_list[instruction_address - 1] = str(self._accumulator)
                continue

            # ADD instruction
            elif instruction_type == InstructionType.ADD.value:
                self._accumulator = Add.execute(self._accumulator, int(self._memory_list[instruction_address - 1]))
                continue

            # SUBTRACT instruction
            elif instruction_type == InstructionType.SUBTRACT.value:
                self._accumulator = Subtract.execute(self._accumulator, int(self._memory_list[instruction_address - 1]))
                continue

            # DIVIDE instruction
            elif instruction_type == InstructionType.DIVIDE.value:
                try:
                    self._accumulator = Divide.execute(self._accumulator, int(self._memory_list[instruction_address - 1]))
                except ZeroDivisionError:
                    self.memory_error = MemoryError(MET.ZERO_DIVISION, self._instruction_pointer + 1, instruction)
                    return MemoryStatus.ERROR
                continue

            # MULITPLY instruction
            elif instruction_type == InstructionType.MULTIPLY.value:
                self._accumulator = Multiply.execute(self._accumulator, int(self._memory_list[instruction_address - 1]))
                continue

            # BRANCH instruction
            elif instruction_type == InstructionType.BRANCH.value:
                self._instruction_pointer = instruction_address - 1
                continue

            # BRANCHNEG instruction
            elif instruction_type == InstructionType.BRANCH_NEG.value:
                if BranchNeg.execute(self._accumulator):
                    self._instruction_pointer = instruction_address - 1
                continue

            # BRANCHZERO instruction
            elif instruction_type == InstructionType.BRANCH_ZERO.value:
                if BranchZero.execute(self._accumulator):
                    self._instruction_pointer = instruction_address - 1
                continue

            # HALT instruction
            elif instruction_type == InstructionType.HALT.value:
                return MemoryStatus.HALT

            else:
                raise Exception("bad memory logic")
        