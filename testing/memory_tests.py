import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.memory.memory import Memory, MemoryStatus

class MemoryTests:
    # this class holds our pytest memory unit tests
    pass


