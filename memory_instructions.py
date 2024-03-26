from enum import Enum

class InstructionType(Enum):
    READ = "10"
    WRITE = "11"
    LOAD = "20"
    STORE = "21"
    ADD = "30"
    SUBTRACT = "31"
    DIVIDE = "32"
    MULTIPLY = "33"
    BRANCH = "40"
    BRANCH_NEG = "41"
    BRANCH_ZERO = "42"
    HALT = "43"

class Add:
    @staticmethod
    def execute(accumulator, value):
        return accumulator + value

class Subtract:
    @staticmethod
    def execute(accumulator, value):
        return accumulator - value

class Divide:
    @staticmethod
    def execute(accumulator, value):
        if value == 0:
            raise ZeroDivisionError
        return accumulator / value

class Multiply:
    @staticmethod
    def execute(accumulator, value):
        return accumulator * value

class BranchNeg:
    @staticmethod
    def execute(accumulator):
        return accumulator < 0

class BranchZero:
    @staticmethod
    def execute(accumulator):
        return accumulator == 0
