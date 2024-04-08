from abc import ABC, abstractmethod
from enum import Enum

class MemoryErrorType(Enum):
    INSTRUCTION_FORMAT = "instruction format error"
    INSTRUCTION_RANGE = "instruction range error"
    MEMORY_RANGE = "memory range error"
    ZERO_DIVISION = "zero division error"
    NUMBER_CONVERSION = "int conversion error"
    ACCUMULATOR_CONVERSION = "accumlator conversion error"

class MemoryError(ABC):
    def __init__(self, line_num = 0, instruction = "", data = ""):
        self._line_num = line_num         # The memory line when the error occured
        self._instruction = instruction   # The current instruction when the error occured
        self._data = data                 # Additional information that involved with the error

    @abstractmethod
    def description(self):
        pass

class InstructionFormatError(MemoryError):
    def description(self):
        return "\nProgram Stopped (Invalid instruction format of \"{0}\" at line {1})".format(self._instruction, self._line_num)
    
class InstructionRangeError(MemoryError):
    def description(self):
        return "\nProgram Stopped (Instruction address \"{0}\" at line {1} is outside memory range)".format(self._instruction, self._line_num)
    
class MemoryRangeError(MemoryError):
    def description(self):
        return "\nProgram Stopped (Instruction traversal reached end of memory)"
    
class ZeroDivError(MemoryError):
    def description(self):
        return "\nProgram Stopped (Divide operation \"{0}\" at line {1} resulted in zero divisor)".format(self._instruction, self._line_num)
    
class NumberConversionError(MemoryError):
    def description(self):
        return "\nProgram Stopped (Arithmetic operation \"{0}\" at line {1} could not operate on value \"{2}\")".format(self._instruction, self._line_num, self._data)
    
class AccumulatorConversionError(MemoryError):
    def description(self):
        return "\nProgram Stopped (Load operation \"{0}\" at line {1} could not convert value \"{2}\")".format(self._instruction, self._line_num, self._data)

# Alternatively could have the init inside each child class depending on what they need. Something like this?
# class InstructionFormatError(MemoryError):
#     def __init__(self, line_num=0, instruction=""):
#         self._line_num = line_num
#         self._instruction = instruction

#     def description(self):
#         return "\nProgram Stopped (Invalid instruction format of \"{0}\" at line {1})".format(self._instruction, self._line_num)

# class InstructionRangeError(MemoryError):
#     def __init__(self, instruction=""):
#         self._instruction = instruction

#     def description(self):
#         return "\nProgram Stopped (Instruction address \"{0}\" is outside memory range)".format(self._instruction)
        