import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.memory.memory import Memory
from src.memory.memory_instructions import Add, Subtract, Divide, Multiply, BranchNeg, BranchZero
import re

class MemoryTests:
    # this class holds our pytest memory unit tests
    
    def test_init(self):
        mem = Memory(["+2099", "+4300"])
        assert len(mem._memory_list) == Memory.MAX_MEMORY_SIZE
        assert mem._memory_list[0] == "+2099"
        assert mem.memory_error is None
        assert mem._accumulator == 0
        assert mem._instruction_pointer == 0
        assert mem._IO_address == 0

    def test_memory_regex(self):
        mem1 = Memory(["+2099", "+4300"])
        assert re.search(mem1._instruction_regex, "+4286") is not None
        assert re.search(mem1._instruction_regex, "+42086") is None

        mem2 = Memory(["+11045", "+43000"])
        assert re.search(mem2._instruction_regex, "+42086") is not None
        assert re.search(mem2._instruction_regex, "+4286") is None

    def test_add_operation(self):
        result = Add.execute(50, 10)
        assert result == 60

    def test_subtract_operation(self):
        result = Subtract.execute(50, 10)
        assert result == 40

    def test_divide_operation(self):
        result = Divide.execute(50, 10)
        assert result == 5

    def test_multiply_operation(self):
        result = Multiply.execute(50, 10)
        assert result == 500

