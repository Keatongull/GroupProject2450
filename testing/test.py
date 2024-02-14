from memory import Memory

# unit tests will go here



def test_read_function():
    p1 = Memory()
    p1.parse_file("Test1.txt")
    # This doesn't use the actual read function read function needs input
    # idk how to do that without breaking pytest. Instead it has the same functionality
    newWord = +1032
    p1.memDict["99"] = newWord
    assert p1.memDict == "+1032"

def test_write_function():
    p1 = Memory()
    p1.write("99")
    assert p1.memDict["99"] == 86

def test_load_function():
    p1 = Memory()
    p1.parse_file("Test1.txt")
    p1.load("1")
    assert p1.accumulator == "+1007"

def test_store_function():
    p1 = Memory()
    p1.accumulator = 86
    p1.load("50")
    assert p1.memDict["50"] == 86