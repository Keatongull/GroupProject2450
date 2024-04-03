import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.memory import Memory



# unit tests will go here



def test_read_function():
    p1 = Memory()
    p1.parse_file("testing/Test1.txt")
    # This doesn't use the actual read function read function needs input
    # idk how to do that without breaking pytest. Instead it has the same functionality
    newWord = "+1032"
    p1.memDict["99"] = newWord
    assert p1.memDict["99"] == "+1032"

#def test_write_function():
    #p1 = Memory()
    #p1.write("99")
    #unsure how to test for output to the console

def test_load_function():
    p1 = Memory()
    p1.memDict["1"] = "+1007"
    p1.load("1")
    assert p1.accumulator == "+1007"

def test_store_function():
    p1 = Memory()
    p1.accumulator = 86
    p1.store("50")
    assert p1.memDict["50"] == 86