
#add abstract class?

class Read:
    pass

class Write:
    pass

class Load:
    pass

class Store:
    pass

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
