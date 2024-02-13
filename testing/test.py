import memory

# unit tests will go here



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