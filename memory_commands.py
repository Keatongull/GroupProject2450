
#add abstract class?

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
