
from enum import Enum

class MemoryErrorType(Enum):
    INSTRUCTION_FORMAT = "instruction format error"
    INSTRUCTION_RANGE = "instruction range error"
    MEMORY_RANGE = "memory range error"
    ZERO_DIVISION = "zero division error"
    INT_CONVERSION = "int conversion error"

class MemoryError():
    def __init__(self, error_type, line_num = 0, instruction = "", data = ""):
        self._error_type = error_type     # The MemoryErrorType
        self._line_num = line_num         # The memory line when the error occured
        self._instruction = instruction   # The current instruction when the error occured
        self._data = data                 # Additional information that involved with the error

    def description(self):
        if self._error_type == MemoryErrorType.INSTRUCTION_FORMAT:
            return "\nProgram Stopped (Invalid instruction format of \"{0}\" at line {1})".format(self._instruction, self._line_num)
        elif self._error_type == MemoryErrorType.INSTRUCTION_RANGE:
            return "\nProgram Stopped (Instruction address \"{0}\" at line {1} is outside memory range)".format(self._instruction, self._line_num)
        elif self._error_type == MemoryErrorType.MEMORY_RANGE:
            return "\nProgram Stopped (Instruction traversal reached end of memory)"
        elif self._error_type == MemoryErrorType.ZERO_DIVISION:
            return "\nProgram Stopped (Divide operation \"{0}\" at line {1} resulted in zero divisor)".format(self._instruction, self._line_num)
        elif self._error_type == MemoryErrorType.INT_CONVERSION:
            return "\nProgram Stopped (Arithmetic operation \"{0}\" at line {1} could not operate on value \"{2}\")".format(self._instruction, self._line_num, self._data)
        